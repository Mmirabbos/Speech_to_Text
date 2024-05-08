import pandas as pd
from pydub import AudioSegment
import speech_recognition as sr
import os

s = sr.Recognizer()

data = {"audio": [], "transcribe": []}

books_path = os.listdir(r"C:\Users\mirabbos\Desktop\qwerty\books")

original_path = r"C:\Users\mirabbos\Desktop\qwerty\books"

wav_audio = os.listdir(r'C:\Users\mirabbos\Desktop\qwerty\wav_audio')

wav_audio_path = r'C:\Users\mirabbos\Desktop\qwerty\wav_audio'


def convert(path):
    if not os.path.exists("wav_audio"):
        os.makedirs("wav_audio")
    
    for i in path:
        audio_path = os.path.join(original_path, i)
        sound = AudioSegment.from_file(audio_path, format="m4a")
        wav_file_path = audio_path.replace('.m4a', '.wav')
        sound.export(wav_file_path, format="wav")

# convert(books_path) Books ichidagi audiolar m4a formatda edi


def cutting(path):
    audio = AudioSegment.from_file(path)
    print(audio) 
    i = 0

    while i < len(audio):
        cuting = audio[i:i + 60000]
        save = os.path.join("wav_audio", f"{name.replace(".wav", '')}_{i}.wav")
        cuting.export(save, format="wav")
        data["audio"].append(save.replace("wav_audio\\", ''))
        i += 60000

for name in books_path:
    print(name)
    file_path = os.path.join(original_path, name)
    cutting(file_path)

def transcribe(audio):
    audio_path = os.path.join(original_path, audio)
    with sr.AudioFile(audio_path) as file:
        audio_data = s.record(file)
        try:
            print(audio)
            text = s.recognize_google(audio_data, language="uz-UZ", show_all=False)
            data["transcribe"].append(text)
        except sr.UnknownValueError:
            print("Error")

for name in wav_audio:
    audio_path = os.path.join(wav_audio_path, name)
    transcribe(audio_path)

df = pd.DataFrame(data)

print(data)