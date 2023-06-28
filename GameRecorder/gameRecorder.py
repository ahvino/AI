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
import pyautogui
import cv2
import numpy as np
from moviepy.editor import * #VideoFileClip, AudioFileClip, concatenate_videoclips
import os
from textblob import TextBlob
from textblob import Word


root = tkinter.Tk()
root.geometry("1000x750")
root.title('Game Recorder')
root.config(bg="grey")
root.maxsize(1000, 750)

left_frame = Frame(root, width=200, height=700)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=700, height=700)
#right_frame = Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=5)



dateNTime = datetime.now()
date = dateNTime.strftime("%d_%m_%Y_%H_%M_%S")
recorderAudioFile = "output_" + date
recorderAudioText = "output_" + date + ".txt"
recString = StringVar()

onOff = False
cheatImage = Image.open('GameRecorder\cheater.png')
cheatResize = cheatImage.resize((400,400))
cheatResize.save('GameRecorder\cheater.png')

ggImage = Image.open('GameRecorder\goodgamer.png')
cheatResize = ggImage.resize((400,400))
cheatResize.save('GameRecorder\goodgamer.png')

onImg = ImageTk.PhotoImage(file='GameRecorder\on.png')
offImg = ImageTk.PhotoImage(file='GameRecorder\off.png')
cheatImg = ImageTk.PhotoImage(file='GameRecorder\cheater.png')
ggImg = ImageTk.PhotoImage(file='GameRecorder\goodgamer.png')

def CreateAudioVideo(audioFile, videoFile):
    video_clip = VideoFileClip(videoFile)
    audio_clip = AudioFileClip(audioFile)
    
    final_clip = video_clip.set_audio(audio_clip)
    name = "Cheater_Clip_" + videoFile
    #codec = cv2.VideoWriter_fourcc(*"XVID")
    final_clip.write_videofile(name, codec="libx264")
    

def ScreenRecorder():
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    dateNTime = datetime.now()
    date = dateNTime.strftime("%d_%m_%Y_%H_%M_%S")
    filename =  date + ".mp4"
    fps = 30.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    
    fs = 44100
    seconds = 15 
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        out.write(frame)
        
        cv2.imshow('Live', frame)
        
        if cv2.waitKey(1) == ord('q'):
            sd.stop()
            write(recorderAudioFile + ".wav", fs, recording)

            break
        
    out.release()
    cv2.destroyAllWindows()
    CreateAudioVideo(recorderAudioFile + ".wav", filename)

    

def StartRecFunc():
    ScreenRecorder()

    recString.set("Recording complete")
    LeftBtn = tkinter.Button(left_frame, image = onImg, command=RecorderFunc).grid(row=1, column=0, padx=5, pady=5)

   
   
def RecorderFunc():
    global onOff
    global onImg 
    global offImg 
    if (onOff):
        print("setting to true")
        #LeftBtn(left_frame, image= onImg)
        LeftBtn = tkinter.Button(left_frame, image = onImg, command=RecorderFunc).grid(row=1, column=0, padx=5, pady=5)
        onOff = False 
        recString.set("Now recording...")
        t1 = threading.Thread(target=StartRecFunc)
        t1.start()
    else:
        print("setting to false")     
        LeftBtn = tkinter.Button(left_frame, image = offImg, command=RecorderFunc).grid(row=1, column=0, padx=5, pady=5)
        onOff = True
 
 
def TranslateFunc():
    recString.set("Transcribing...")
    print("Entered RunTranslater")
    model = whisper.load_model("base")
    audio = whisper.load_audio(recorderAudioFile + ".wav")
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    file = open(recorderAudioText, "a")
    file.write(result.text)
    file.close()   
    recString.set("Transcription complete!")
    CheckForCheaters(recorderAudioText)
    
    
def CheckForCheaters(recorderAudioText):
    file = open(recorderAudioText, "r")
    fileOutput = file.readlines()
    file.close()
    cheater = TextBlob(fileOutput.__str__())
    found = -1
    found = cheater.find("cheat")
    if (found > -1):
        cheaterLbl = Label(right_frame, image = cheatImg, width=500, height=500).grid(row=4, column=0, padx=5, pady=5)
    else:
        cheaterLbl = Label(right_frame, image = ggImg, width=500, height=500).grid(row=4, column=0, padx=5, pady=5)

       
def RunTranslater():
    recString.set("Transcribing...")
    print("Entered RunTranslater")
    time.sleep(1)
    t2 = threading.Thread(target=TranslateFunc())
    t2.start()
    
def ExitFunc():
    quit()


outputStr= "Output: "
recString.set("Not Recording")

playinglabel = Label(left_frame, textvariable=recString, relief=RAISED).grid(row=0, column=0, padx=5, pady=5)
LeftBtn = tkinter.Button(left_frame, image = offImg, command=RecorderFunc).grid(row=1, column=0, padx=5, pady=5)
RightBtn = tkinter.Button(left_frame, text="Translate", command=RunTranslater).grid(row=1, column=1, padx=5, pady=5)
outputLbl = Label(left_frame, text=outputStr).grid(row=2, column=0, padx=5, pady=5)
quitBtn = tkinter.Button(left_frame, text="Quit", command=lambda:ExitFunc()).grid(row=3, column=0, padx=5, pady=5)
cheaterLbl = Label(right_frame, image = "").grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
