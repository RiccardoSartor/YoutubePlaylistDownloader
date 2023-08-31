import re
from pytube import Playlist
import os, sys

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
DOWNLOAD_DIR = desktop + '\\music'

argv = sys.argv[1:]

playlist = Playlist(argv[0])

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print('tracks: ' + str(len(playlist.video_urls)))

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)