import re
from pytube import Playlist
import os, sys
import win32clipboard as clip

clip.OpenClipboard()
data = clip.GetClipboardData()
clip.CloseClipboard()

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
DOWNLOAD_DIR = desktop + '\\music'

'''
argv = sys.argv[1:] #exclude from te pharameters command: "python app.py" or "app.exe"

if "app=desktop&" in argv[0]:
    argv[0] = argv[0].replace("app=desktop&", "")

playlist = Playlist(argv[0]) #get playlist link from the pharameters
'''
playlist = Playlist(data)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print('downloading ' + str(len(playlist.video_urls)) + " tracks")

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)