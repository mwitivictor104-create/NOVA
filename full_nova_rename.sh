#!/bin/bash
set -euo pipefail

PROJECT_DIR="$HOME/NOVA"
BACKUP_DIR="${PROJECT_DIR}_backup_full_rename_$(date +%s)"

echo "==> Backing up $PROJECT_DIR to $BACKUP_DIR ..."
cp -a "$PROJECT_DIR" "$BACKUP_DIR"
echo "==> Backup complete."

echo "==> STEP 1: Fixing Android package (com.NOVA.bubble -> com.nova.bubble) ..."

# 1a. Update package declarations/imports inside Kotlin, XML, Gradle files
find "$PROJECT_DIR" -type f \( -name "*.kt" -o -name "*.xml" -o -name "*.gradle" \) -not -path "*/.git/*" | while read -r f; do
    if grep -q "com\.NOVA\." "$f" 2>/dev/null; then
        sed -i 's/com\.NOVA\./com.nova./g' "$f"
        echo "   package ref updated: $f"
    fi
done

# 1b. Move the actual folder(s) named .../com/NOVA/... to .../com/nova/...
find "$PROJECT_DIR" -depth -type d -path "*/com/NOVA*" -not -path "*/.git/*" | while read -r d; do
    newd=$(echo "$d" | sed 's#/com/NOVA#/com/nova#')
    if [ -e "$newd" ]; then
        echo "   WARNING: target exists, merging manually needed: $newd"
    else
        mkdir -p "$(dirname "$newd")"
        mv "$d" "$newd"
        echo "   moved: $d -> $newd"
    fi
done

echo "==> STEP 1 complete."

echo "==> STEP 2: General NOVA -> NOVA rename (contents) across the rest of the project ..."

find "$PROJECT_DIR" -type f -not -path "*/.git/*" | while read -r f; do
    case "$f" in
        *.png|*.jpg|*.jpeg|*.gif|*.webp|*.zip|*.jar|*.so|*.dex|*.class|*.apk|*.aab|*.ico|*.exe|*.bin|*.pyc)
            continue
            ;;
    esac
    if file "$f" | grep -qi text; then
        if grep -qiE "NOVA" "$f" 2>/dev/null; then
            sed -i -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g' "$f"
        fi
    fi
done
echo "==> STEP 2 content replacement complete."

echo "==> STEP 3: Renaming any remaining files/folders containing 'NOVA' ..."

find "$PROJECT_DIR" -depth -iname "*NOVA*" -not -path "*/.git/*" | while read -r path; do
    dir=$(dirname "$path")
    base=$(basename "$path")
    new_base=$(echo "$base" | sed -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g')
    if [ "$base" != "$new_base" ]; then
        new_path="$dir/$new_base"
        if [ -e "$new_path" ]; then
            echo "   WARNING: target exists, skipping: $new_path"
        else
            mv "$path" "$new_path"
        fi
    fi
done

echo ""
echo "==> ALL DONE."
echo "    Backup kept at: $BACKUP_DIR"
echo "    Project updated in place at: $PROJECT_DIR"
