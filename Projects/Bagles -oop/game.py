from bagles import Bagles


gameExit = False


while not gameExit:
    print("Enter Difficulty ( 1 to 9 or r for random ):")
    diff = input()
    game = Bagles(diff)
    secret_number_list = game.newGame
    SECRET_NUMBER = ''

    for number in secret_number_list:
        SECRET_NUMBER += str(number)

    mistakes = 0

    print("I have a number now...")
    gameWon = False

    while not gameWon:
        print("Enter your guess: ")
        guess = input()

        while not game.validateInput(guess):
            print("Enter a {}-digit number!".format(str(diff)))
            guess = input()

        guess_list = list(guess)
        clues = []

        if int(guess) == int(SECRET_NUMBER):
            gameWon = True
            print("You have won!")
            print("Do you want to play again ?! ( Y / N )")
            playAgain = input()
            if playAgain.upper() == 'N':
                gameExit = True
            else:
                gameExit = False
            break

        for i in range(len(secret_number_list)):
            if int(guess_list[i]) == secret_number_list[i]:
                clues.append("Fermi")
            elif int(guess_list[i]) in secret_number_list:
                clues.append("Pico")
            else:
                clues.append("Bagels")
        mistakes += 1
        print("Mistakes : {}".format(str(mistakes)))
        print(clues)

        if mistakes > 10:
            print("You Lost !!")
            print("The number was {}".format(str(SECRET_NUMBER)))
            print("Do you want to play again ?! ( Y / N )")
            playAgain = input()
            if playAgain.upper() == 'N':
                gameExit = True
            else:
                gameExit = False
            break

print("Bye!")
