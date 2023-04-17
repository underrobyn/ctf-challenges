#!/bin/bash

/usr/bin/python3 /root/randomly-populate.py

dir_path="/srv/ftp/tmp"

# Remove all files but keep the 100 most recent ones
find "$dir_path" -type f -name "*.tmp" -printf "%T@ %p\0" \
 | sort -znr | awk -v RS='\0' -F ' ' 'NR > 100 {sub("^[^ ]* ",""); print}' | xargs -0 rm -f

chmod -R 777 "$dir_path"
