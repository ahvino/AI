from tkinter import *
from textblob import TextBlob
from tkinter import ttk
import wikipediaapi
import nltk


tk = Tk()

tk.geometry("800x400")



def display_text():
    global entry1, entry2
    
    string1= entry1.get()
    string2= entry2.get()
    
    label1.configure(text=string1)
    label2.configure(text=string2)
    
    wiki = wikipediaapi.Wikipedia('en')
    
    page_py1 = wiki.page(string1)
    page_py2 = wiki.page(string2)

    #print("Summary: " + page_py1.summary)
    #print("Summary: " + page_py2.summary)
    
    sent1 = TextBlob(page_py1.summary)
    sent2 = TextBlob(page_py2.summary)
    
    print(sent1.sentiment)
    print(sent2.sentiment)
    
    print(sent1.polarity)
    print(sent2.polarity)
    
    if sent1.polarity > sent2.polarity:
        str1 = string1 + " is more favorable than " + string2
        label3 = Label(tk, text=str1, font=("Courier 22 bold"))
        label3.pack()
    else:
        str2 = string2 + " is more favorable than " + string1
        label3 = Label(tk, text=str2, font=("Courier 22 bold"))
        label3.pack()
    

    
    
#Initialize a Label to display the User Input
label1=Label(tk, text="", font=("Courier 22 bold"))
label1.pack()

label2=Label(tk, text="", font=("Courier 22 bold"))
label2.pack()

#Create an Entry widget to accept User Input
entry1= Entry(tk, width= 40)
entry1.focus_set()
entry1.pack()

entry2= Entry(tk, width= 40)
entry2.focus_set()
entry2.pack()

#Create a Button to validate Entry Widget
ttk.Button(tk, text= "Okay",width= 20, command= display_text).pack(pady=20)

tk.mainloop()