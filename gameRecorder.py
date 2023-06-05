"""
Selik Samai
MS 548
Python Project 

For my project, I'd like to create a tool that can be used while gaming to get
key information and record it for analysis later on. For instance, if you 
suspect someone is cheating, you can start the application and dictate what 
you're seeing, user names, and any messages you're receiving on your end. I 
don't think I'll be able to get all of it done but I think I can definitely
implement some of the features. So far, I've looked into using both whisper and
pytorch for this. Currently I'll focus more so on the dictation and 
transcribing of what's occurring.  I think the process will be as follows:
1. Use Tkinter to create base application. 
2. Record data
3. Upon completion of recording use whisper to transcribe the data. 
4. Analyze the data. 

API Libraries
-------------------
chocolatey, 
pytorch
whisper
Tkinter
ffmpeg
scipy
numpy
"""

import whisper 
import sounddevice as sd
from scipy.io.wavfile import write
import tkinter
import tkinter.messagebox
from tk import *
from tkinter import *
import threading
import time

top = tkinter.Tk()
top.geometry("600x300")
top.title('Main Menu')


recString = StringVar()

onOff = False
onImg = PhotoImage(file = "on.png")
offImg = PhotoImage(file = "off.png")


def StartRecFunc():
    fs = 44100
    seconds = 10 
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, recording)
    recString.set("Recording complete")
    LeftBtn.config(image= offImg)  
   



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
    
    audio = whisper.load_audio("output.wav")
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    
    
    file = open("transcript.txt", "a")
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

    