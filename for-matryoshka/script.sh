#!/bin/bash

# Switch to data dir
cd /data || exit 1

# Ensure required tools are installed
command -v tar >/dev/null 2>&1 || { echo >&2 "tar is required but not installed. Aborting."; exit 1; }
command -v gzip >/dev/null 2>&1 || { echo >&2 "gzip is required but not installed. Aborting."; exit 1; }
command -v rar >/dev/null 2>&1 || { echo >&2 "rar is required but not installed. Aborting."; exit 1; }
command -v zip >/dev/null 2>&1 || { echo >&2 "zip is required but not installed. Aborting."; exit 1; }
command -v genisoimage >/dev/null 2>&1 || { echo >&2 "genisoimage is required but not installed. Aborting."; exit 1; }
command -v xz >/dev/null 2>&1 || { echo >&2 "xz is required but not installed. Aborting."; exit 1; }
command -v bzip2 >/dev/null 2>&1 || { echo >&2 "bzip2 is required but not installed. Aborting."; exit 1; }
command -v 7z >/dev/null 2>&1 || { echo >&2 "7z is required but not installed. Aborting."; exit 1; }
command -v compress >/dev/null 2>&1 || { echo >&2 "compress is required but not installed. Aborting."; exit 1; }
command -v lzip >/dev/null 2>&1 || { echo >&2 "lzip is required but not installed. Aborting."; exit 1; }
command -v lz4 >/dev/null 2>&1 || { echo >&2 "lz4 is required but not installed. Aborting."; exit 1; }
command -v zstd >/dev/null 2>&1 || { echo >&2 "zstd is required but not installed. Aborting."; exit 1; }

# Set the name of the file we want to archive
FILENAME="/data/flag.txt"

# Archive flag.txt with tar
tar -cf flag.tar $FILENAME

# Archive the resulting file with gz
gzip -c flag.tar > flag.tar.gz

# Archive the resulting file with rar
rar a flag.tar.gz.rar flag.tar.gz

# Archive the resulting file with zip
zip flag.tar.gz.rar.zip flag.tar.gz.rar

# Archive the resulting file with iso
genisoimage -o flag.tar.gz.rar.zip.iso -J -r flag.tar.gz.rar.zip

# Archive the resulting file with xz
xz -z -c flag.tar.gz.rar.zip.iso > flag.tar.gz.rar.zip.iso.xz

# Archive the resulting file with bzip2
bzip2 -z -c flag.tar.gz.rar.zip.iso.xz > flag.tar.gz.rar.zip.iso.xz.bz2

# Archive the resulting file with 7z
7z a flag.tar.gz.rar.zip.iso.xz.bz2.7z flag.tar.gz.rar.zip.iso.xz.bz2

# Archive the resulting file with z (compress)
compress -c flag.tar.gz.rar.zip.iso.xz.bz2.7z > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z

# Archive the resulting file with lz
lzip -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz

# Archive the resulting file with lz4
lz4 -z -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4

# Archive the resulting file with zstd
zstd -z -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4 > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4.zst

# move final file
cp flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4.zst /mnt/data/final.zst
