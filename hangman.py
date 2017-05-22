import random, string, os
LOGO = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                              
'''

DIVIDER = '-='
DIVIDER_REPEAT_TIMES = 30
WORDS = 'cat dog snake elephant horse dinosaur fish bird eagle'.split()
wrong_letters = []
correct_letters = []
mistakes = 0

HANGMANPICS = ['''
+---+
|   |
|
|
|
|
=========
''',

'''
+---+
|   |
|   O
|
|
|
=========
''',

'''
+---+
|   |
|   O
|   |
|
|
=========
''',

'''
+---+
|   |
|   O
|  /|
|  
|
=========
''',

'''
+---+
|   |
|   O
|  /|\
|  
|
=========
''', 

'''
+---+
|   |
|   O
|  /|\
|  /
|
=========
''',

'''
+---+
|   |
|   O
|  /|\
|  / \
|
=========
''']


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# randomWord
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def randomWord(wordList):
    random_index = random.randint(0, len(wordList) - 1)
    return wordList[random_index]
# =======================================


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# displayBoard
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def displayBoard(mistakesCounter, secretWord):
    print("Wrong: ", mistakesCounter)
    print("Remaining: ", len(HANGMANPICS) - mistakesCounter)
    print("Wrong Letters:", [letter + ' ' for letter in wrong_letters])
    print(DIVIDER * DIVIDER_REPEAT_TIMES)
    print(HANGMANPICS[mistakesCounter])
    print()
    displayBlanks(secretWord)
    print()
# =======================================


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# displayBlanks
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def displayBlanks(secretWord):
    blanks = ''
    for i in range(len(secretWord)):
        if secretWord[i] in correct_letters:
            blanks += secretWord[i] + ' '
        else:
            blanks += '_ '
    print(blanks)
# =======================================


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# clearScreen
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def clearScreen():
    _= os.system('cls')
# =======================================


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# gameIntro
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def gameIntro():
    print(LOGO)
    print(DIVIDER * DIVIDER_REPEAT_TIMES)
# =======================================


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# verifyLetter
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def verifyLetter(letter):
    if len(letter) > 1:
        print("enter only 1 letter!")
    elif letter in wrong_letters:
        print("you already guessed this letter! guess another")
    elif letter not in string.ascii_lowercase:
        print("please enter a LETTER")
    else:
        return True
# =======================================

secret_word = randomWord(WORDS)
print("SECRET WORD IS", secret_word)


while True:
    gameIntro()
    displayBoard(mistakes, secret_word)
    print("Enter a letter: ")
    user_letter = input()

    while not verifyLetter(user_letter):
        user_letter = input()
        verifyLetter(user_letter)

    clearScreen()

    if user_letter in secret_word:
        correct_letters.append(user_letter)
        displayBoard(mistakes, secret_word)
        gameWon = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                gameWon = False
                break

        if gameWon:
            print("YES! the word was {}".format(secret_word))
            print("WooHoo!!! You won :D")
            input()
            break

        else:
            clearScreen()
            displayBoard(mistakes, secret_word)

    else:
        clearScreen()
        if mistakes >= len(HANGMANPICS) - 1:
            print("The man was hanged :(")
            print("YOU LOSE !")
            print("The word was {}".format(secret_word))
            input()
            break
        else:
            mistakes += 1        
            displayBoard(mistakes, secret_word)
            wrong_letters.append(user_letter)