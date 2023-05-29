import tkinter
import tkinter.messagebox
from tk import *
from textblob import TextBlob
from textblob import Word
from datetime import datetime
import textblobExample

top = tkinter.Tk()
top.geometry("600x300")
top.title('Main Menu')


# Option 5 function
def ExitFunc():
    quit()


Outputtext = tkinter.Text(top, height= 10, width = 10)

menuText = """ Main Menu \n 
1. Spell Checker \n
2. Words in a sentence \n
3. Word Count \n
4. Word definition \n
5. Exit"""
#Lbl = tkinter.Label(text=menuText)

def OutputMessage(text):
    tkinter.messagebox.showinfo(title="Info", message=text)


def InputWarning():
    tkinter.messagebox.showwarning(title="Warning", message="No input entered. Please try again.")




def StartFunc(option):
    run = True
    selection = option
    #while run == True: 
    input = RightTextBox.get("1.0",'end-1c')

    if selection == 0:
        if(input):
            value = textblobExample.SpellCheckFunc(input)     
            OutputMessage(value)       
        else:
            InputWarning()           
        CleanInput()   
               
    elif selection == 1:
        print("Option 2")
        var = textblobExample.SentenceFunc(input)
        OutputMessage(var) 
        CleanInput()
        
    elif selection == 2:
        print("Option 3")
        var = textblobExample.GetWordCount(input)
        cw = textblobExample.CWords()
        dateNTime = datetime.now()
        date = dateNTime.strftime("%d/%m/%Y %H:%M:%S")
        cw.summary = date + "\n" + "Get Sentence Function: \nTotal words and breakdown are as follows " + var.__str__() + "\n=======================================\n"    
        textblobExample.WriteToFileFunc("TextBlobFunctions.txt", cw.summary)    
        OutputMessage(cw.summary)
        CleanInput()
        
    elif selection == 3:
        print("Option 4")
        var = textblobExample.DefineFunc(input)
        cw = textblobExample.CWords()
        cw.TextWrite(var)
        OutputMessage(var)
        CleanInput()
        
    elif selection == 4:
        ExitFunc()
    else:
        print("You entered an invalid menu option. Please try again.")
    
        




def callback(event):
    selection = event.widget.curselection()[0]
    run = True
    StartFunc(selection)
        
def getInput():
    inputTxt = RightTextBox.get("1.0",'end-1c')
    print(inputTxt)

def CleanInput():
    RightTextBox.delete("1.0",'end-1c')

lbOptions = tkinter.Listbox()

lbOptions.insert(0, "1. Spell Checker")
lbOptions.insert(1, "2. Words in a Sentence")
lbOptions.insert(2, "3. Words count")
lbOptions.insert(3, "4. Word definition")
lbOptions.insert(4, "5. Exit")

lbOptions.bind('<Double-1>', callback)


LeftTextBox = tkinter.Text(top, height=15, width=30)
LeftTextBox.insert(tkinter.INSERT, menuText)




RightTextBox = tkinter.Text(top, height=10, width=20)
enterBtn = tkinter.Button(top, text="Enter", command=lambda: getInput())

LeftTextBox.pack(side="left")
RightTextBox.pack(side="right")
enterBtn.pack(side="bottom")
lbOptions.pack()


top.mainloop()