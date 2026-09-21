#!/bin/bash
set -euo pipefail

SRC="$HOME/Nitron/GeneratedProjects/calculator"
DEST="$HOME/NOVA/NovaWatch"

if [ ! -d "$SRC" ]; then
    echo "ERROR: source not found at $SRC"
    exit 1
fi

echo "==> Copying calculator app to $DEST ..."
mkdir -p "$DEST"
cp -a "$SRC/." "$DEST/"
echo "==> Copy complete."

echo "==> Renaming app label to NovaWatch in strings.xml/manifest ..."
find "$DEST" -type f \( -name "strings.xml" -o -name "AndroidManifest.xml" \) | while read -r f; do
    sed -i 's/Nitron *Calculator/NovaWatch/gI; s/>Calculator</>NovaWatch</g' "$f"
done

echo "==> Fixing package: com.nitron.app -> com.novawatch.app in code files ..."
find "$DEST" -type f \( -name "*.kt" -o -name "*.xml" -o -name "*.gradle" \) | while read -r f; do
    if grep -q "com\.nitron\.app" "$f" 2>/dev/null; then
        sed -i 's/com\.nitron\.app/com.novawatch.app/g' "$f"
        echo "   package ref updated: $f"
    fi
done

echo "==> Moving folder structure com/nitron/app -> com/novawatch/app ..."
find "$DEST" -depth -type d -path "*/com/nitron/app" | while read -r d; do
    newd=$(echo "$d" | sed 's#/com/nitron/app#/com/novawatch/app#')
    mkdir -p "$(dirname "$newd")"
    mv "$d" "$newd"
    echo "   moved: $d -> $newd"
done
# clean up now-empty com/nitron if left behind
find "$DEST" -depth -type d -empty -path "*/com/nitron" -exec rmdir {} \; 2>/dev/null || true

echo "==> Remaining generic nitron -> NOVA cleanup ..."
find "$DEST" -type f | while read -r f; do
    case "$f" in
        *.png|*.jpg|*.jpeg|*.gif|*.webp|*.zip|*.jar|*.so|*.dex|*.class|*.apk|*.aab|*.ico|*.exe|*.bin|*.pyc)
            continue ;;
    esac
    if file "$f" | grep -qi text; then
        if grep -qiE "nitron" "$f" 2>/dev/null; then
            sed -i -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g' "$f"
        fi
    fi
done
find "$DEST" -depth -iname "*nitron*" | while read -r path; do
    dir=$(dirname "$path")
    base=$(basename "$path")
    new_base=$(echo "$base" | sed -E 's/[Nn][Ii][Tt][Rr][Oo][Nn]/NOVA/g')
    if [ "$base" != "$new_base" ]; then
        mv "$path" "$dir/$new_base" 2>/dev/null || true
    fi
done

echo ""
echo "==> DONE. NovaWatch app created at: $DEST"
