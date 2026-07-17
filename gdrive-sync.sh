#!/bin/bash
set -euo pipefail

TARGET="rug:Documents/Teaching/The Psychology of Judgment and Decision-Making"
MD_DIR="input/md"
CHAPTERS_DIR="input/md/chapters"
REFS_DIR="references"
SVG_DIR="input/svg"

usage() {
    echo "Usage: $0 <command> [command ...]"
    echo ""
    echo "Commands:"
    echo "  push   Push md, reference, and svg files to Google Drive"
    echo "  pull   Pull md files from Google Drive"
    echo "  diff   Diff local md files against pulled txt files"
    echo ""
    echo "Commands can be combined, e.g.: $0 push pull diff"
    exit 1
}

clean_txt() {
    sed -i '1s/^\xEF\xBB\xBF//' "$1"
    sed -i 's/\r$//' "$1"
}

squeeze_blanks() {
    # Condense 3+ consecutive newlines to exactly 2 (one blank line). This avoid
    # empty lines fro accumulating due to repeated conversion to and from Google
    # Docs.
    find "$1" -name "*.txt" -exec perl -0777 -pi -e 's/\n{3,}/\n\n/g' {} +
}

push_mds() {
    local src_dir="$1"
    local dst="$2"
    local tmp
    tmp=$(mktemp -d)
    for mdfile in "$src_dir"/*.md; do
        [ -f "$mdfile" ] || continue
        cp "$mdfile" "$tmp/$(basename "${mdfile%.md}").txt"
    done
    squeeze_blanks "$tmp"
    rclone delete "$dst" --max-depth 1 2>/dev/null || true
    rclone copy "$tmp" "$dst" \
        --drive-import-formats txt \
        --drive-allow-import-name-change
    rm -rf "$tmp"
}

do_push() {
    echo "=== PUSH input md files ==="
    push_mds "$MD_DIR" "$TARGET"
    echo "Done"

    echo ""
    echo "=== PUSH chapter md files ==="
    push_mds "$CHAPTERS_DIR" "$TARGET/chapters"
    echo "Done"

    echo ""
    echo "=== PUSH references (md and bib files) ==="
    rclone delete "$TARGET/references" 2>/dev/null || true
    local tmp
    tmp=$(mktemp -d)
    find "$REFS_DIR" \( -name "*.md" -o -name "*.bib" \) | while read -r srcfile; do
        dir=$(dirname "$srcfile")
        mkdir -p "$tmp/$dir"
        txtfile="${srcfile%.*}.txt"
        cp "$srcfile" "$tmp/$txtfile"
    done
    squeeze_blanks "$tmp"
    rclone copy "$tmp/$REFS_DIR" "$TARGET/references" \
        --drive-import-formats txt \
        --drive-allow-import-name-change
    rm -rf "$tmp"
    echo "Done"

    echo ""
    echo "=== PUSH references (pdf files) ==="
    rclone copy "$REFS_DIR" "$TARGET/references" --include "*.pdf"
    echo "Done"

    echo ""
    echo "=== PUSH svg files ==="
    rclone copy "$SVG_DIR" "$TARGET/svg" --include "*.svg"
    echo "Done"
}

do_pull() {
    echo "=== PULL md files ==="
    rclone copy "$TARGET" "$MD_DIR" \
        --include "*.txt" \
        --max-depth 1 \
        --drive-export-formats txt
    rclone copy "$TARGET/chapters" "$CHAPTERS_DIR" \
        --include "*.txt" \
        --max-depth 1 \
        --drive-export-formats txt
    for txtfile in "$MD_DIR"/*.txt "$CHAPTERS_DIR"/*.txt; do
        [ -f "$txtfile" ] || continue
        clean_txt "$txtfile"
    done
    echo "Done"
}

do_diff() {
    echo "=== DIFF ==="
    local changed_files=()
    for mdfile in "$MD_DIR"/*.md "$CHAPTERS_DIR"/*.md; do
        [ -f "$mdfile" ] || continue
        local txtfile="${mdfile%.md}.txt"
        if [ ! -f "$txtfile" ]; then
            echo "⚠️  $mdfile — no matching .txt file (run pull first)"
            continue
        fi
        if diff -B "$mdfile" "$txtfile" > /dev/null; then
            echo "✅ $mdfile — identical"
        else
            echo "❌ $mdfile — differs:"
            diff -B "$mdfile" "$txtfile" || true
            echo ""
            changed_files+=("$mdfile")
        fi
    done
    echo ""
    if [ ${#changed_files[@]} -eq 0 ]; then
        echo "✅ All files are identical!"
        return
    fi
    echo "❌ ${#changed_files[@]} file(s) differ"
    echo ""
    read -rp "Merge changes? Overwrites .md files with .txt files [y/N] " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        for mdfile in "${changed_files[@]}"; do
            local txtfile="${mdfile%.md}.txt"
            cp "$txtfile" "$mdfile"
            echo "✅ Merged: $txtfile → $mdfile"
        done
        echo ""
        echo "Merge complete"
    else
        echo "No changes made"
    fi
}

# --- Main ---

if [ $# -eq 0 ]; then
    usage
fi

for cmd in "$@"; do
    case "$cmd" in
        push) do_push ;;
        pull) do_pull ;;
        diff) do_diff ;;
        *) echo "Unknown command: $cmd"; usage ;;
    esac
done