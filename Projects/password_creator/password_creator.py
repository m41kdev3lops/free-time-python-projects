import os

vic_name = input("Enter vic name ( initials are better ): ")
file_name = 'potential_passwords_for_' + str(vic_name) + '.txt'

while True:
    if os.path.isfile(file_name):
        opt = print("A file already exists for this victim. Please rename your existing file!")
        input("Click Enter when done!")
    else:
        file_handler = open(file_name, 'w')
        break

potential_pw = input("Enter potential password ( :stop to stop or :quit to quit )")
all_pws = list()

while potential_pw:
    if potential_pw == ':exit':
        file_handler.close()
        exit(0)
    elif potential_pw == ':stop':
        break
    else:
        all_pws.append(potential_pw)
        potential_pw = input("Enter potential password ( :stop to stop or :quit to quit )")

for i, pw in enumerate(all_pws):
    file_handler.write(pw + "\n")
    all_pws_clone = all_pws[:]
    del all_pws_clone[i]

    for ipw in all_pws_clone:
        temp_pass = pw + ipw
        file_handler.write(temp_pass + "\n")

print("Writing Complete")
file_handler.close()
exit(0)