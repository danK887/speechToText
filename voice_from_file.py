import json
import wave
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

wf = wave.open("123.wav", "rb")
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