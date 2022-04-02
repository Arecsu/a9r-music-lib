#!/bin/bash

no_media() {
   echo $1
   touch "$1/.NOMEDIA"
}


export -f no_media

echo "Working..."

# excludes hidden directories and shows not empty dirs
# but it will include directores with other directories inside
# >>>>>>
# find $1 -mindepth 1 \( ! -regex '.*/\..*' \) -not -empty -type d | parallel --jobs 2 no_media {}

# excludes hidden directories and shows dirs with at least one file
find $1 -mindepth 2 -not -path '*/.*' -type f -print0 | xargs -0 -n 1 dirname | sort -u | parallel --jobs 2 no_media {}

# folders that contain jpg, png or opus
# then sed will leave just the directory path without the file
# sort will sort it
# uniq will remove duplicates
# >>>>>>>>
# find . -type f \( -iname \*.jpg -o -iname \*.png -o -iname \*.opus \) | sed -r 's|/[^/]+$||' |sort |uniq



