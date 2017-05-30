class Caesar:
    def __init__(self, msg, key):
        self.msg = msg
        self.key = key


    def setMessage(self, msg):
        self.msg = msg


    def encrypt(self):
        msg_list = self.msg.split()
        final_msg_list = []
        encrypted = ''

        for word in msg_list:
            if int(msg_list.index(word)) == int(len(msg_list) - 1):
                final_msg_list.append(word)
            else:
                final_msg_list.append(word + ' ')

        del msg_list

        for word in final_msg_list:
            word_list = list(word)
            for character in word_list:
                char_ascii = ord(character)
                if (127 - char_ascii) <= self.key:
                    new_char_ascii = int(char_ascii) - 5
                else:
                    new_char_ascii = int(char_ascii) + self.key
                encrypted += chr(new_char_ascii)

        del char_ascii, word_list, character, word
        return encrypted


    def decrypt(self):
        msg_list = self.msg
        decrypted = ''

        word_list = list(msg_list)

        for character in word_list:
            char_ascii = ord(character)
            if (127 - (char_ascii) + 5) <= self.key:
                new_char_ascii = int(char_ascii) + 5
            else:
                new_char_ascii = int(char_ascii) - self.key
            decrypted += chr(new_char_ascii)

        del char_ascii, word_list, character
        return decrypted