#!/bin/bash

# optimized folder structure for bandcamp zip files
# ./$artist/$album/{files extracted here}
process_zip() {
   file=$1
   album=$(echo ${file#*\ -})
   album=$(echo ${album%.zip})
   artist=$(echo ${file%%\ -*})
   artist=${artist:2}

   directory="./$artist/$album"
   mkdir -p "$directory"
   unzip -o -d "$directory" "$file"

   # echo $artist - $album

}

export -f process_zip

# jobs = number of threads
# if you have a modern cpu + hard disk drive, use just 1
# otherwise, with an SSD or even better NVME you can increase that
# by a lot, probably all the available cores of your system.

# maxdepth to 1 so it won't explore subfolders
find . -maxdepth 1 -name "*.zip" | parallel --jobs 1 process_zip {}
