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
5. Use screen recording for video
6. Use Audio recording
7. Combine audio and video 
8. Translate and determine if speech indicates a cheater is playing. 


https://www.thepythoncode.com/article/make-screen-recorder-python
https://www.geeksforgeeks.org/create-a-screen-recorder-using-python/
https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
API Libraries
-------------------
chocolatey, 
pytorch
whisper
Tkinter
ffmpeg
scipy
numpy
cv2
moviepy
pyautogui
threading
scipy
sounddevice
