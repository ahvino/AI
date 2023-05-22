from textblob import TextBlob
from textblob import Word
from datetime import datetime

# Selik Samai
# MS 548 Advanced Programming Concepts and AI. 
# Python project 1

# I estimate the most lengthy part of this assignment is understanding TextBlob.
# Part of the issue I expect to have is understanding the usage of the libraries.
# I also had trouble with getting everything setup too. Coming up with useful functions 
# was a little difficult too as some of the stuff seemed trivial and could be done
# without the use of the textblob library, but it would be significantly more code to do so. 
# There was also some getting used to the Python language. some of ti was pretty trivial but 
# printing some of the values was a little more difficult than I expected.

# I was right about textblob being the most cumbersome. Overall the entire project took just
# under 5 hours from start to finish which is what I expected it to take. 

"""
For the next iteration of my project, I;d like to try and use Tkinter for a GUI for my application. 
I think I can extend a lot of the functionality of the menus to work on larger sets of data like from
a website. I can possibly add something that will allow me to search for certain words in say a blog 
post and thatword can be user customizable. I'd like to also have the output read back to the user as 
well and possibly have audio cues when processing a response that is correct or incorrect. 
"""

###############################################################################
class CWords:
    
    def __init__(self):
        self.cfilename = ""       
        self.summary = ""
        self.tuple = ()
        
    def TextRead():   
        txtSummary = open("TextBlobFunctions.txt", "r")        
        print(txtSummary.read())
    
    def TextWrite(self, tuple):
        dateNTime = datetime.now()
        date = dateNTime.strftime("%d/%m/%Y %H:%M:%S") 
        wrd = tuple[0]
        definition = tuple[1]
        
        values = wrd + ": " + str(definition)
        summary = date.__str__() + "\n" + "Definition function: "+ values + "\n=======================================\n" 
        WriteToFileFunc("TextBlobFunctions.txt", summary)
        
        
        
###############################################################################    
class cIncorrectWords(CWords):
    def __init__(self):
        super().__init__()
        self.cfilename = "IncorrectWords.txt"
            
        # Add a data asa dictionary to the summary
    def AddToSummary(self, text):    
        cw = cIncorrectWords()
        
        dateNTime = datetime.now()
        date = dateNTime.strftime("%d/%m/%Y %H:%M:%S")
        summary = date + "\n" + text + "\n=======================================\n"    
        WriteToFileFunc(cw.cfilename, summary)
###############################################################################
class cCorrectWords(CWords):
    def __init__(self):
        super().__init__()
        self.cfilename = "CorrectWords.txt"
        
    def AddToSummary(self,text):    
        cw = cCorrectWords()
        print("Text: " + text)
        print ("filename: " + cw.cfilename)
        dateNTime = datetime.now()
        date = dateNTime.strftime("%d/%m/%Y %H:%M:%S")
        print ("data: " + date)
        summary = date + "\n" + text + "\n=======================================\n"    
        print(summary)

        WriteToFileFunc(cw.cfilename, summary)

###############################################################################


###############################################################################

def MenuOptionFunc():
    print("==============================================================")
    print("Main Menu")
    print("1. Spell checker")
    print("2. Words in a sentence")
    print("3. Word count")
    print("4. Word definition")
    print("5. Exit")
    print ("Enter menu options 1-4 for textblob examples. Enter 5 to Exit")
    print("==============================================================")


def WriteToFileFunc(filename, outputTxt):
    file = open(filename, "a")   
    file.write(outputTxt + "\n")   
    file.close()
    
    
def ExitFunc():
    quit()

def SpellCheckFunc():
    words = input("Please enter a word for the Spell Check Function: ")
    if words.isalpha() == True:
        var = TextBlob(words)
        if words == var.correct():
            correct = cCorrectWords()
            text = "Spell Check Function: \n" + "'" + words + "' was spelled correctly"
            correct.AddToSummary(text)
            
        else:
            incorrect = cIncorrectWords()
            text = "Spell Check Function: \n" + "'" + words + "' was spelled incorrectly"
            incorrect.AddToSummary(text)      
    else:
        print("The input was not a valid word.")
        SpellCheckFunc()


def SentenceFunc():
    sentence = input("Enter a sentence and we'll provide the words in the sentence. ")
    var = WordsListFunc(sentence)
    WriteToFileFunc("TextBlobFunctions.txt", "Sentence Function result: " + var.__str__())
    


def WordsListFunc(words):
    sentence = TextBlob(words)
    var = sentence.words
    return var



def GetSentence():
    sentence = input("Enter in the sentence. ")
    return sentence
        
    

def GetWordCount(words):
    var = TextBlob(words)
    return var.word_counts


def DefineFunc():
    word = input("Enter in a word and we'll define the word. ")
    var = TextBlob(word)
    definition = Word(word).define()
  
    cw = CWords()
    cw.tuple = (word, definition)
    return cw.tuple
    

def StartFunc():
    MenuOptionFunc()
    run = True
    menuVal = input("Enter your menu option choice: ")
    while run == True:
        if menuVal == '1':            
            SpellCheckFunc()
        elif menuVal == '2':
            SentenceFunc()
        elif menuVal == '3':
            var = GetSentence()
            if not var == False:
                var = GetWordCount(var)
                cw = CWords()
                dateNTime = datetime.now()
                date = dateNTime.strftime("%d/%m/%Y %H:%M:%S")
                cw.summary = date + "\n" + "Get Sentence Function: \nTotal words and breakdown are as follows " + var.__str__() + "\n=======================================\n"    
                print("Total words and breakdown are as follows: ")
                print(var)
                WriteToFileFunc("TextBlobFunctions.txt", cw.summary)
        elif menuVal == '4':
            var = DefineFunc()
            cw = CWords()
            cw.TextWrite(var)
        elif menuVal == '5':
            print("     Option 5")
            run == False
            ExitFunc()
        else:
            print("You entered an invalid menu option. Please try again.")
        StartFunc()

StartFunc()

            
        


