#!/bin/bash

# 128 bitrate works awesome with opus
# can't tell between flac and opus in ABX test

flac_to_opus() {
   # flacpath="$1"
   opuspath="${1::-5}.opus"

   # basename=$(basename "$1" .flac)
   # echo works faster compared to basename :)
   basename=$(echo ${1##*/})

   echo "→ $basename"
   opusenc --vbr --bitrate 128 --quiet "$1" "$opuspath"
}

export -f flac_to_opus
# can increase jobs if your cpu and storage can handle it
find $1 -name "*.flac" | parallel --jobs 8 flac_to_opus {}
