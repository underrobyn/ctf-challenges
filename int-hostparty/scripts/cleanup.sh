#!/bin/bash

dir_path="/path/to/directory"

# Remove all files but keep the 100 most recent ones
find "$dir_path" -type f -printf "%T@ %p\0" | sort -znr | awk -v RS='\0' -F ' ' 'NR > 100 {sub("^[^ ]* ",""); print}' | xargs -0 rm -f
