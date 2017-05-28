import random

mistakes = 0

INTRO = '''
██████╗  █████╗  ██████╗ ██╗     ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝ ██║     ██╔════╝██╔════╝
██████╔╝███████║██║  ███╗██║     █████╗  ███████╗
██╔══██╗██╔══██║██║   ██║██║     ██╔══╝  ╚════██║
██████╔╝██║  ██║╚██████╔╝███████╗███████╗███████║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
'''

DIVIDER = '-*-'

RULES = '''
To play Bagles, the computer thinks of a 3-digit number.
You have to guess the digits in 10 guesses in order to win.
There are some clues for the game;

** Pico -> One digit is correct but in the wrong position,
** Fermi -> One digit is correct and in the right position,
** Bagels -> No digit is correct.

Have Fun :)
'''
print(INTRO)
print(DIVIDER * 20)
print(RULES)
print(DIVIDER * 20)


def getRandomNumber():
    ORIG_NUMS = list(range(10))
    random.shuffle(ORIG_NUMS)
    SECRET_NUM_LIST = ORIG_NUMS[:3]
    SECRET_NUM = ''.join(str(num) for num in SECRET_NUM_LIST)
    return SECRET_NUM


def validateUserInput(input):
    try:
        int(input)
        input = str(input)
        if len(input) != 3:
            return False
        return True
    except:
        return False

print(DIVIDER * 15)
SECRET_NUM = getRandomNumber()
SECRET_NUM_LIST = list(SECRET_NUM)
print("I have thought of a number... ")

gameWon = False

while not gameWon:
    print("Enter your guess:")
    guess = input()
    while not validateUserInput(guess):
        print("Please enter a 3-digit number!")
        guess = input()
        validateUserInput(guess)

    guess_list = list(guess)
    clues = []

    if guess == SECRET_NUM:
        print(DIVIDER * 30)
        print("GratZ!! You've won!")
        print("The number was : " + str(SECRET_NUM))
        gameWon = True
    else:
        if mistakes >= 10:
            print(DIVIDER * 30)
            print("You have lost :(")
            print("The number was : " + str(SECRET_NUM))
            exit(0)
        for i in range(len(guess)):
            if guess_list[i] == SECRET_NUM_LIST[i]:
                clues.append('FERMI')
            elif guess_list[i] in SECRET_NUM_LIST:
                clues.append('PICO')
            else:
                clues.append("BAGLES")
        mistakes += 1
        print(DIVIDER * 20)
        print("Mistakes : " + str(mistakes))
        clue_string = ''
        for clue in clues:
            clue_string += clue + ' '

        print(clue_string)