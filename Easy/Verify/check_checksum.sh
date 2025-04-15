KNOWN_CHECKSUM="your_known_checksum_here"
FOLDER="./your_folder_here"

find "$FOLDER" -type f -exec sha256sum {} + | while read checksum file; do
    if [[ "$checksum" == "$KNOWN_CHECKSUM" ]]; then
        echo "[MATCH] $file"
    else
        echo "[MISMATCH] $file"
    fi
done

