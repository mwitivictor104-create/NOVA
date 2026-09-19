#!/bin/bash
set -euo pipefail

PROJECT_DIR="$HOME/NOVA"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "ERROR: '$PROJECT_DIR' is not a directory."
    exit 1
fi

BACKUP_DIR="${PROJECT_DIR%/}_backup_before_nova_rename"

echo "==> Backing up '$PROJECT_DIR' to '$BACKUP_DIR' ..."
if [ -e "$BACKUP_DIR" ]; then
    echo "ERROR: backup dir '$BACKUP_DIR' already exists. Remove/rename it first."
    exit 1
fi
cp -a "$PROJECT_DIR" "$BACKUP_DIR"
echo "==> Backup complete."

echo "==> Replacing text occurrences of NOVA (any case) inside files ..."

find "$PROJECT_DIR" -type f -not -path "*/.git/*" | while read -r f; do
    case "$f" in
        *.png|*.jpg|*.jpeg|*.gif|*.webp|*.zip|*.jar|*.so|*.dex|*.class|*.apk|*.aab|*.ico|*.exe|*.bin|*.pyc)
            continue
            ;;
    esac
    if file "$f" | grep -qi text; then
        if grep -qiE "NOVA" "$f" 2>/dev/null; then
            sed -i -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g' "$f"
            echo "   updated contents: $f"
        fi
    fi
done

echo "==> Renaming files and directories containing 'NOVA' (any case) ..."

find "$PROJECT_DIR" -depth -iname "*NOVA*" -not -path "*/.git/*" | while read -r path; do
    dir=$(dirname "$path")
    base=$(basename "$path")
    new_base=$(echo "$base" | sed -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g')
    if [ "$base" != "$new_base" ]; then
        new_path="$dir/$new_base"
        if [ -e "$new_path" ]; then
            echo "   WARNING: target already exists, skipping: $new_path"
        else
            mv "$path" "$new_path"
            echo "   renamed: $path -> $new_path"
        fi
    fi
done

echo ""
echo "==> Done."
echo "    Backup kept at: $BACKUP_DIR"
echo "    Updated project at: $PROJECT_DIR"
