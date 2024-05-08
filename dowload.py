from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v=Qdyl85S5FS8&t=268s&ab_channel=Audiokitob'

yt = YouTube(url)

video = yt.streams.filter(only_audio=True)

audio = video[0]

if not os.path.exists("audio"):
    os.makedirs("audio")

audio.download(output_path='audio', filename='audio')
