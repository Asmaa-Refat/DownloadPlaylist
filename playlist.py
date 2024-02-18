# pip3 install pytube
# to run -->  python3 <filename>.py
from pytube import Playlist, YouTube
from tkinter import filedialog
import sys
import re

playlist_url = input("Hey dude, Can you please enter the YouTube playlist URL: ")
url_pattern = r'^https?://(?:www\.)?(?:youtube\.com/playlist\?list=|youtu\.be/)([a-zA-Z0-9_-]+)$'

# Check if the input matches the playlist URL pattern
if not re.match(url_pattern, playlist_url):
    print("Please enter a valid YouTube playlist URL next time!!")
    sys.exit() 

# Load the playlist - Create Playlist obj
playlist = Playlist(playlist_url)

# Print the total number of videos in the playlist
print("Total videos in the playlist: ", len(playlist.video_urls))

# Choose the directory to save the videos
path = filedialog.askdirectory()

if not path:
    print("please choose a folder next time!!")
    sys.exit() 

# Loop through each video in the playlist and download it
for video_url in playlist.video_urls:
    video = YouTube(video_url) #getting the youtube video from the url
    print("Yaay Downloading:", video.title)
    video.streams.get_highest_resolution().download(output_path=path)

print("============================================================================")
print("All the videos in the playlist have been downloaded successfully!.. Enjooy 😉")
