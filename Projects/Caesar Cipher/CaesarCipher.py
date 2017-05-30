import os
from CaesarClass import Caesar


os.system('cls')

INTRO = '''
 _____                              _____ _       _               
/  __ \                            /  __ (_)     | |              
| /  \/ __ _  ___  ___  __ _ _ __  | /  \/_ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| \__/\ (_| |  __/\__ \ (_| | |    | \__/\ | |_) | | | |  __/ |   
 \____/\__,_|\___||___/\__,_|_|     \____/_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    
'''
DIVIDER = '-=-'

print(INTRO)
print(DIVIDER * 15)

print('Enter Mode .. ( E or D )')
mode = input()

while mode.upper() not in ['E', 'D', 'ENCRYPT', 'DECRYPT']:
    print("Enter either ( E or D )")
    mode = input()


if mode in ['E', 'ENCRYPT']:
    print("Enter message to Encrypt: ")
    msg = input()
    print("Enter Key ( 1 - 15 )")
    key = input()
    while int(key) not in list(range(1, 15)):
        print("Enter a valid key!")
        key = input()

    caesar = Caesar(str(msg), int(key))
    print("Encrypted : %s" %caesar.encrypt())

elif mode in ['D', 'DECRYPT']:
    print("Enter message to Decrypt: ")
    msg = input()
    print("Enter Encryption Key:")
    key = input()
    while int(key) not in list(range(1, 15)):
        print("Enter a valid encryption key!")
        key = input()

    caesar = Caesar(str(msg), int(key))
    print("Decrypted: %s" %caesar.decrypt())

exit(0)