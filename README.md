Collection of scripts and stuff that I use to handle my local music library 🎷

# Bandcamp

### 📂 Chrome extension to download every purchase

[This extension](https://chrome.google.com/webstore/detail/bandcamp-auto-downloader/igbcekbalgomjoblhoehkemlcapkfaki/). Not developed by me. Works *fine*.

Just wait for every download link to be ready and run the extension. Don't lose the focus on the browser tab for too long. If possible, leave it always on top.

### 🗃️ unzip-bandcamp-parallel.sh

Unzip every bandcamp zip file into my chosen folder structure (./$artist/$album)

With support for multithread unzip process. Tweak the number of threads inside the script. With 2+, it will nuke pretty much any HDD, so use 2+ only with SSD/NVMEs.

# Last.fm

### 🖼️ artist-images-lastfm.py

Get all the images from Last.fm of a given artist. Multithreaded. Tweak the number of parallel downloads inside the script.

[Gist previously published here](https://gist.github.com/Arecsu/2a96c33b4a99705d7711dee77156e2c2)

### 🖼️ artist-images-lastfm-bandcamp.py

Ugly modification to the original script to make it work for my music library folder structure, for every artist automatically.

Yeah, really ugly code. The download bars don't even show up correctly. It's a mess. But it works!

# Local files management

### 🎸 flac-to-opus.sh

Search for FLAC files in folder and subfolders and converts them to .opus files.

Opus compression is insanely good. Can't tell between FLAC and 128 kbps Opus. Seriously, it's THAT good 😱

Uses multithread. Tweak the number of parallel conversions inside the script depending on your storage and cpu speed.

### ❌ Delete all FLAC files

After I convert everything to Opus, I run this line to get rid of all FLAC files in folder and subfolders

```
find . -name "*.flac" -type f -delete
```


