from textblob import TextBlob
from textblob import Word





def MenuOptionFunc():
    print("==============================================================")
    print("Main Menu")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
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



def GetSentenceAndLangFunc():
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
            var = GetSentenceAndLangFunc()
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

            
        


