#!/bin/bash
set -euo pipefail

SRC="$HOME/NOVA"
DEST="$HOME/NOVA/merged_from_NOVA"

if [ ! -d "$SRC" ]; then
    echo "ERROR: source '$SRC' not found."
    exit 1
fi

echo "==> Copying everything from $SRC into $DEST ..."
mkdir -p "$DEST"
cp -a "$SRC/." "$DEST/"
echo "==> Copy complete."

echo "==> Replacing text occurrences of NOVA (any case) inside files ..."
find "$DEST" -type f -not -path "*/.git/*" | while read -r f; do
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
echo "==> Text replacement done."

echo "==> Renaming files and folders containing 'NOVA' (any case) ..."
find "$DEST" -depth -iname "*NOVA*" -not -path "*/.git/*" | while read -r path; do
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
echo "==> Done."
echo "    NOVA content merged into: $DEST"
echo "    All 'NOVA' text/names inside it renamed to 'NOVA'."
