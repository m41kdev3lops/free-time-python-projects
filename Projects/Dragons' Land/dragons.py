import random, time


gamePlay = True


def displayIntro():
    print("You are in a land filled with dragons")
    print("They live in caves where the sun can't reach them")
    print("Some of the dragons are friendly and can share their treasure with you")
    print("Other dragons are greedy, hungry and more dragon-ly")
    print("You are facing two cave entrances")
    print("You have to choose a cave ...")
    print()


def displayCaveEntrance():
    print("You walked towards the cave entrance....")
    time.sleep(2)
    print("It is dark, spooky and has weird sounds")
    time.sleep(2)
    print("You see a dragon walking towards you.....")
    time.sleep(2)
    print("And Then it.... !!!")
    time.sleep(2)
    
    

while gamePlay:
    goodCave = random.randint(1, 2)

    displayIntro()
    print("Which cave would you like to go into? (1 or 2)")
    playerChosenCave = int(input())
    if playerChosenCave == goodCave:
        displayCaveEntrance()
        print("Smiles at you and gives you his treasure :)")
        time.sleep(1)
        print("Congratulations! you have won")
    else:
        displayCaveEntrance()
        print("Starts howling at you!")
        time.sleep(1)
        print("You keep running ....")
        time.sleep(3)
        print("No Way Out!!! You are trapped.")
        time.sleep(2)
        print("You are terrified as you see the dragon approaches ...")
        time.sleep(2)
        print("You then see it opens its mouth and ......")
        time.sleep(2)
        print("Complete darkness.....")
        time.sleep(1)
        print("You Lost :(")

    print()
    print("Do you want to play again? (yes or no)")
    playAgain = str(input()).lower()

    if playAgain in ['yes', 'y']:
          gamePlay = True
    else:
          gamePlay = False




exit(0)







        
