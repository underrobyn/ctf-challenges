#!/bin/bash

# Set the name of the file we want to archive
FILENAME="flag.txt"

# Create an array of archive formats we want to use
FORMATS=("tar.gz" "rar" "zip" "iso" "xz" "bz2" "7z" "z" "sit")

# Loop through the archive formats and create archives
for FORMAT in "${FORMATS[@]}"
do
    # Create the archive using tar and the current format
    tar -cf "$FILENAME.tar" "$FILENAME"

    # Compress the tar archive using gzip
    gzip "$FILENAME.tar"

    # Create the archive using the current format and the gzip-compressed tar file
    case $FORMAT in
        tar.gz)
            mv "$FILENAME.tar.gz" "$FILENAME.$FORMAT"
            ;;
        rar)
            7z a -m0=lzma2 -mx=9 -mfb=64 -md=32m -ms=on "$FILENAME.$FORMAT" "$FILENAME.tar.gz"
            rm "$FILENAME.tar.gz"
            ;;
        zip)
            7z a -tzip "$FILENAME.$FORMAT" "$FILENAME.tar.gz"
            rm "$FILENAME.tar.gz"
            ;;
        iso)
            mkisofs -o "$FILENAME.$FORMAT" "$FILENAME.tar.gz"
            rm "$FILENAME.tar.gz"
            ;;
        xz)
            xz "$FILENAME.tar"
            mv "$FILENAME.tar.xz" "$FILENAME.$FORMAT"
            ;;
        bz2)
            bzip2 "$FILENAME.tar"
            mv "$FILENAME.tar.bz2" "$FILENAME.$FORMAT"
            ;;
        7z)
            7z a "$FILENAME.$FORMAT" "$FILENAME.tar.gz"
            rm "$FILENAME.tar.gz"
            ;;
        z)
            compress "$FILENAME.tar"
            mv "$FILENAME.tar.Z" "$FILENAME.$FORMAT"
            ;;
        sit)
            stuff "$FILENAME.tar"
            mv "$FILENAME.tar.sit" "$FILENAME.$FORMAT"
            ;;
        *)
            echo "Unsupported format: $FORMAT"
            ;;
    esac

    # Print a message indicating that the archive was created
    echo "Created archive: $FILENAME.$FORMAT"
done
