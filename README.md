Collection of scripts and stuff that I use to handle my local music library ๐ท

# Bandcamp

### ๐ Chrome extension to download every purchase

[This extension](https://chrome.google.com/webstore/detail/bandcamp-auto-downloader/igbcekbalgomjoblhoehkemlcapkfaki/). Not developed by me. Works *fine*.

1. Wait for every download link to be ready and run the extension
2. Configure the browser to accept every download automatically in a specific folder
3. Don't lose the focus on the browser tab for too long. If possible, leave it always on top.
4. ???
5. Download everything

### ๐๏ธ unzip-bandcamp-parallel.sh

Unzip every bandcamp zip file into my chosen folder structure (./$artist/$album)

With support for multithread unzip process. Tweak the number of threads inside the script. With 2+, it will nuke pretty much any HDD, so use 2+ only with SSD/NVMEs.

# Last.fm

### ๐ผ๏ธ artist-images-lastfm.py

Get all the images from Last.fm of a given artist. Multithreaded. Tweak the number of parallel downloads inside the script.

[Gist previously published here](https://gist.github.com/Arecsu/2a96c33b4a99705d7711dee77156e2c2)

### ๐ผ๏ธ artist-images-lastfm-bandcamp.py

Ugly modification to the original script to make it work for my music library folder structure, for every artist automatically.

Yeah, really ugly code. The download bars don't even show up correctly. It's a mess. But it works!

# Local files management

### ๐ธ flac-to-opus.sh

Search for FLAC files in folder and subfolders and converts them to .opus files.

Opus compression is insanely good. Can't tell between FLAC and 128 kbps Opus. Seriously, it's THAT good ๐ฑ

Uses multithread. Tweak the number of parallel conversions inside the script depending on your storage and cpu speed.

### โ Delete all FLAC files

After I convert everything to Opus, I run this line to get rid of all FLAC files in folder and subfolders

```
find . -name "*.flac" -type f -delete
```

### ๐งจ no-media.sh

Creates a `.NOMEDIA` file inside all subfolders of a given path. Android will exclude the folder from gallery apps and such
