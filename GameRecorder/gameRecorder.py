import sounddevice as sd
from scipy.io.wavfile import write
import tkinter
import tkinter.messagebox
from tk import *
from tkinter import *
import threading
import time
import whisper 
from datetime import datetime
from PIL import Image, ImageTk


top = tkinter.Tk()
top.geometry("600x300")
top.title('Main Menu')


dateNTime = datetime.now()
date = dateNTime.strftime("%d_%m_%Y_%H_%M_%S")
recorderAudioFile = "output_" + date + ".wav"
recorderAudioText = "output_" + date + ".txt"
recString = StringVar()

onOff = False
onImg = ImageTk.PhotoImage(file='GameRecorder\on.png')
offImg = ImageTk.PhotoImage(file='GameRecorder\off.png')


def StartRecFunc():
    fs = 44100
    seconds = 10 
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(recorderAudioFile, fs, recording)
    recString.set("Recording complete")
    LeftBtn.config(image= onImg)  
   



def RecorderFunc():
    global onOff
    if (onOff):
        print("setting to true")
        LeftBtn.config(image= onImg)
        onOff = False 
        recString.set("Now recording...")
        t1 = threading.Thread(target=StartRecFunc)
        t1.start()
    else:
        print("setting to false")
        LeftBtn.config(image= offImg)  
        onOff = True
 
 
def TranslateFunc():
    recString.set("Transcribing...")
    print("Entered RunTranslater")
    model = whisper.load_model("base")
    audio = whisper.load_audio(recorderAudioFile)
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    
    
    file = open(recorderAudioText, "a")
    file.write(result.text)
    file.close()   
    recString.set("Transcription complete!")
  
        
def RunTranslater():
    recString.set("Transcribing...")
    print("Entered RunTranslater")
    time.sleep(1)
    t2 = threading.Thread(target=TranslateFunc())
    t2.start()
    
def ExitFunc():
    quit()

LeftBtn = tkinter.Button(top, image = offImg, bd = 0, command=RecorderFunc)
RightBtn = tkinter.Button(top, text="Translate", command=RunTranslater)
quitBtn = tkinter.Button(top, text="Quit", command=lambda:ExitFunc())
label = Label(top, textvariable=recString, relief=RAISED)
recString.set("Not Recording")


label.pack(side="top")
LeftBtn.pack(side="left")
RightBtn.pack(side="right")
quitBtn.pack(side="bottom")

top.mainloop()

