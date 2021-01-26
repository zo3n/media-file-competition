# media-file-competition
This Python script creates a competition between media files in certain folder. You get prompted with two different images and/or videos and then you decide which one is better. This cycle repeats until every file has been compared with each other, and then a winner is declared and a scoreboard is shown.

The default location where this script assumes your files are is in **Desktop\\pictures\\** folder.

## Note:
At the time of programming this, I was using it for personal reasons, and wasn't planning on publishing it. However today I am publishing it anyway, but the reason why I am
talking about all of this is because this python script assumes you use **VLC** by default for viewing videos, and **Windows Image Viewer** for viewing images.
(Because it auto closes them after you've voted which media file out of 2 is better). The script will still work fine if you don't use one or both of these programs,
but it won't autoclose them.

I probably should add support for any photo/video viewer being compatible with this, but I'm not really sure how I'd know their process name to close them.
Maybe in the future. Maybe.
