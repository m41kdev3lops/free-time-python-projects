# -*- coding: utf-8 -*-
# ===============================================================================================================================================
# This tool is created by M41k Dev3lops
# Visit My Website : http://maikdevelops.pythonanywhere.com
# GitHub: https://github.com/m41kdev3lops
# !IMPORTANT! Report any bugs or errors on the github repo.
# !IMPORTANT! Feel free to use this software as you see fit as I do NOT hold responsibility for your actions. Use this software on your own risk.
# Enough talk, let's get to the fun stuff!
# ===============================================================================================================================================

# Python Imports
import argparse
import datetime
import sys
import itertools

# Class to store global variables
class Glob:
    ''' Global Variables Class '''
    chr_set = 'abcdefghijklmnopqrstuvwxyz0123456789'
    minimum_length = 4
    maximum_length = 7
    output_file = 'm41k_wordlist_{}.txt'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    verbose = False
    divider = "*"*50

# Functions

# Create the wordlist function
def create_wordlist():
    ''' The heart and soul of the program. A function that creates the whole wordlist '''

    print(Glob.divider)
    print("Generating your passwords now... please wait :]")
    # A local variable to count how many passwords have been added.
    count = 0

    # Open up the file handler with the name specified by the user.
    file_handler = open(Glob.output_file, 'w')

    # This line is the whole meat of the program.
    # itertools.product gets the cartisan product of a set of characters
    # >>> itertools.product('abc')
    # OUTPUT: ('a', 'a') ('a', 'b') ('a', 'c') ('b', 'a') ('b', 'b') ('b', 'c') ('c', 'a') ('c', 'b') ('c', 'c')

    # itertools.chain takes in a method and keeps getting its results until the loop is finished.
    # we specify a for loop for the repeat so it can give us results between our minimum_length and maximum_length values which was specified by the user.
    # we use Glob.maximum_length + 1 as the range function creates numbers from the start UP TO BUT NOT INCLUDING the second number, that's why we have to add one to it.
    for pw in itertools.chain.from_iterable(itertools.product(Glob.chr_set, repeat=i) for i in range(Glob.minimum_length, Glob.maximum_length + 1)):
        # Write the password to the file.
        file_handler.write(''.join(pw) + '\n')
        # Increase local passwords count by 1
        count += 1
        # If verbose is defined then display every single password (would be stupid of the user but an extra option never hurts.)
        if Glob.verbose is True:
            print("[+] {} has been added.".format(''.join(pw)))

    # Close the file handler to free memory.
    # Because i'm a good guy.
    file_handler.close()

    # Footer of the program.
    # Displayed when the program has finished running.
    print(Glob.divider)
    print("{} Passwords have been generated!".format(str(count)))
    print(Glob.divider)
    print("Thanks for using M41k-WLGEN.")
    sys.exit(0)


# The main() function
def main():
    ''' The main function that runs when the program starts running '''

    # Creating the parser
    parser = argparse.ArgumentParser(description='WordList Generator creates word lists for dictionary attacks.')

    # Parser Arguments
    parser.add_argument('chrset', metavar='chrset', nargs="?", help="All possible characters in the passwords you want generated in the wordlist WITHOUT any separation.")   # Characterset Argument
    parser.add_argument('-mn', '--minimumlength', metavar='minlength', nargs="?", type=int, help="The minimum length for the passwords to be generated. Default is 4", default=4)
    parser.add_argument('-mx', '--maximumlength', metavar='maxlength', nargs="?", type=int, help="The maximum length for the passwords to be generated. Default is 7", default=7)
    parser.add_argument('-of', '--outputfile', metavar='outputfile', nargs="?", help="The name of the output file.", default=Glob.output_file)
    parser.add_argument('-v', '--verbose', action='store_true', help="This will show every password while being added to the file. NOT RECOMMENDED BUT IT'S YOUR CALL.", default=None)

    # Parse Args
    args = parser.parse_args()

    # If no arguments passed then print the help.
    # The name of the file itself is considered an argument so that's why we check if the length equals 1 and not 0.
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    # We check the values inputted by the user and we assign them to their apporopriate variables in Glob class.
    if args.minimumlength: Glob.minimum_length = args.minimumlength
    if args.maximumlength: Glob.maximum_length = args.maximumlength
    if args.outputfile: Glob.output_file = args.outputfile
    if args.verbose is not None: Glob.verbose = True
    Glob.chr_set = args.chrset

    # A simple check to make sure that maximum length is > minimum length
    if args.maximumlength != None or args.minimumlength != None:
        if args.minimumlength > args.maximumlength:
            print(Glob.divider)
            print("[-] Dude.. The maximum length can't be less than the minimum length :/")
            sys.exit(0)

    # Create wordlist with the info which we will get from the Glob class.
    create_wordlist()

# If the file is run directly then run the main function.
# This helps prevent running the code if this python file was imported into another python file for example.
if __name__ == "__main__":
    main()
