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
tar -cf flag.1 $FILENAME

# Archive the resulting file with gz
gzip -c flag.1 > flag.1.2

# Archive the resulting file with rar
rar a flag.1.2.3 flag.1.2

# Archive the resulting file with zip
zip flag.1.2.3.4 flag.1.2.3

# Archive the resulting file with iso
genisoimage -o flag.1.2.3.4.5 -J -r flag.1.2.3.4

# Archive the resulting file with xz
xz -z -c flag.1.2.3.4.5 > flag.1.2.3.4.5.6

# Archive the resulting file with bzip2
bzip2 -z -c flag.1.2.3.4.5.6 > flag.1.2.3.4.5.6.7

# Archive the resulting file with 7z
7z a flag.1.2.3.4.5.6.8 flag.1.2.3.4.5.6.7

# Archive the resulting file with z (compress)
compress -c flag.1.2.3.4.5.6.8 > flag.1.2.3.4.5.6.8.9

# Archive the resulting file with lz
lzip -c flag.1.2.3.4.5.6.8.9 > flag.1.2.3.4.5.6.8.9.10

# Archive the resulting file with lz4
lz4 -z -c flag.1.2.3.4.5.6.8.9.10 > flag.1.2.3.4.5.6.8.9.10.11

# Archive the resulting file with zstd
zstd -z -c flag.1.2.3.4.5.6.8.9.10.11 > flag.1.2.3.4.5.6.8.9.10.11.12


### VERIFY SCRIPT

# Switch to data/verify dir
mkdir -p /data/verify
cd /data/verify || exit 1

cp /data/flag.1.2.3.4.5.6.8.9.10.11.12 /data/verify/

# Unarchive zst
zstd -d -c flag.1.2.3.4.5.6.8.9.10.11.12 > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4

# Unarchive lz4
lz4 -d -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4 > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz

# Unarchive lz
lzip -d -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz > flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z

# Unarchive Z (compress)
uncompress -c flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z > flag.tar.gz.rar.zip.iso.xz.bz2.7z

# Unarchive 7z
7z x -so flag.tar.gz.rar.zip.iso.xz.bz2.7z > flag.tar.gz.rar.zip.iso.xz.bz2

# Unarchive bzip2
bzip2 -d -c flag.tar.gz.rar.zip.iso.xz.bz2 > flag.tar.gz.rar.zip.iso.xz

# Unarchive xz
xz -d -c flag.tar.gz.rar.zip.iso.xz > flag.tar.gz.rar.zip.iso

# Unarchive iso
mkdir iso_extract
mount -o loop flag.tar.gz.rar.zip.iso iso_extract
cp iso_extract/flag.tar.gz.rar.zip .
umount iso_extract
rm -r iso_extract

# Unarchive zip
unzip flag.tar.gz.rar.zip

# Unarchive rar
unrar x flag.tar.gz.rar

# Unarchive gz
gzip -d flag.tar.gz

# Unarchive tar to /tmp
tar -xf flag.tar -C /tmp


# move final file
cp flag.tar.gz.rar.zip.iso.xz.bz2.7z.Z.lz.lz4.zst /mnt/data/final.zst
