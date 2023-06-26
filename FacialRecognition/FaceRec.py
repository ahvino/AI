#/Users/seliksamai/repos/AI/AI/FacialRecognition
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
from deepface import DeepFace
from PIL import Image, ImageTk

tk = Tk()

tk.geometry("800x400")

def file_open():
    file = filedialog.askopenfile(mode='r', filetypes=[('Images', '*.jpeg')])
    if file: 
        filepath = os.path.abspath(file.name)
        face_analysis = DeepFace.analyze(img_path=file.name,
            actions = ['age', 'gender', 'race', 'emotion'])
        Label(tk, text="The file is located at : " + str(filepath)).pack()
        Label(tk, text="Emotion: " + face_analysis[0]["dominant_emotion"]).pack()
        Label(tk, text="Race: " + face_analysis[0]["dominant_race"]).pack()
        Label(tk, text="Age: " + str(face_analysis[0]["age"])).pack()


        load = Image.open(file.name)
        render = ImageTk.PhotoImage(load)
        img = Label(tk, image=render)
        img.imaage = render
        img.place(x=300, y=200)
        
        
        #faceImg = PhotoImage(file=file.name)
        #label = Label(tk, image=faceImg)
        #label.pack()


label = Label(tk, text="Click the button to browse the Files")
label.pack(pady=10)

ttk.Button(tk, text="Browse", command=file_open).pack(pady=20)
tk.mainloop()





