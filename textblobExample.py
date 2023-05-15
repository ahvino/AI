from textblob import TextBlob
from textblob import Word
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

def ExitFunc():
    quit()

def SpellCheckFunc():
    words = input("Please enter a word for the Spell Check Function: ")
    if words.isalpha() == True:
        var = TextBlob(words)
        if words == var.correct():
            print(words + " was spelled correctly!")
        else:
            print(words + " was not spelled correctly")        
    else:
        print("The input was not a valid word.")
        SpellCheckFunc()


def SentenceFunc():
    sentence = input("Enter a sentence and we'll provide the words in the sentence. ")
    WordsListFunc(sentence)


def WordsListFunc(words):
    sentence = TextBlob(words)
    var = sentence.words
    print (var)
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
    print(definition)
    

def StartFunc():
    MenuOptionFunc()
    run = True
    menuVal = input("Enter your menu option choice: ")
    while run == True:
        if menuVal == '1':            
            SpellCheckFunc()
            StartFunc()
        elif menuVal == '2':
            SentenceFunc()
            StartFunc()
        elif menuVal == '3':
            var = GetSentence()
            if not var == False:
                var = GetWordCount(var)
            print("Total words and breakdown are as follows: ")
            print(var)
            StartFunc()
        elif menuVal == '4':
            var = DefineFunc()
            StartFunc()
        elif menuVal == '5':
            print("     Option 5")
            run == False
            ExitFunc()
        else:
            print("You entered an invalid menu option. Please try again.")
            StartFunc()

StartFunc()

            
        


