import json
import wave

from vosk import Model, KaldiRecognizer, SetLogLevel


# это нужно для работы с видео.  moviepy - отделяет звуковую дорожку от видео, pydub - преобразует стерео в моно
from moviepy.editor import *
from pydub import AudioSegment

#вытаскиваем из видео звуковую дорожку
audioclip = AudioFileClip("pozhelanie-zamechatelnogo-zimnego-dnja-i-dobrogo-utra.mp4")
audioclip.write_audiofile("our_sound.wav")

#преобразуем звуковую дорожку из стерео в моно
sound = AudioSegment.from_wav("our_sound.wav")
sound = sound.set_channels(1)
sound.export("our_sound.wav", format="wav")

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

wf = wave.open("our_sound.wav", "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)


# You can also init model by name or with a folder path
model = Model(model_name="vosk-model-ru-0.22")
# model = Model("models/en")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass
        #print(rec.Result())
    else:
        pass
        #print(rec.PartialResult())

with open("voice_text.txt", "w", encoding="utf-8") as file:
    rec_text = json.loads(rec.FinalResult())
    file.write(f'{rec_text.get("text")}\n')

print(f'{rec_text.get("text")}')