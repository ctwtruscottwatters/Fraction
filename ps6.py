import string
"""
My first fail week at 6.000.1x
But got the problem set done in rough terms

Charles Truscott Watters for a Massachusetts Institute of Technology passing grade

runfile('C:/Users/17/Downloads/ps6/ps6.py', wdir='C:/Users/17/Downloads/ps6')
Expected Output: jgnnq
Actual Output: jgnnq
Expected Output: (24, 'hello')
Actual Output: HELLO

"""
### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
#    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
#    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dictionary_of_shifts = {}
        ciphertext = ""
        if shift == 'A':
            shift = 1
        elif shift == 'B':
            shift = 2
        elif shift == 'C':
            shift = 3
        elif shift == 'D':
            shift = 4
        elif shift == 'E':
            shift = 5
        elif shift == 'F':
            shift = 6
        elif shift == 'G':
            shift = 7
        elif shift == 'H':
            shift = 8
        elif shift == 'I':
            shift = 9
        elif shift == 'J':
            shift = 10
        elif shift == 'K':
            shift = 11
        elif shift == 'L':
            shift = 12
        elif shift == 'M':
            shift = 13
        elif shift == 'N':
            shift = 14
        elif shift == 'O':
            shift = 15
        elif shift == 'P':
            shift = 16
        elif shift == 'Q':
            shift = 17
        elif shift == 'R':
            shift = 18
        elif shift == 'S':
            shift = 19
        elif shift == 'T':
            shift = 20
        elif shift == 'U':
            shift = 21
        elif shift == 'V':
            shift = 22
        elif shift == 'W':
            shift = 23
        elif shift == 'X':
            shift = 24
        elif shift == 'Y':
            shift = 25
        elif shift == 'Z':
            shift = 26
        elif shift == 'a':
            shift = 27
        elif shift == 'b':
            shift = 28
        elif shift == 'B':
            shift = 2
        elif shift == 'c':
            shift = 29
        elif shift == 'd':
            shift = 30
        elif shift == 'e':
            shift = 31
        elif shift == 'f':
            shift = 32
        elif shift == 'g':
            shift = 33
        elif shift == 'h':
            shift = 34
        elif shift == 'i':
            shift = 35
        elif shift == 'j':
            shift = 36
        elif shift == 'k':
            shift = 37
        elif shift == 'l':
            shift = 38
        elif shift == 'm':
            shift = 39
        elif shift == 'n':
            shift = 40
        elif shift == 'o':
            shift = 41
        elif shift == 'p':
            shift = 42
        elif shift == 'q':
            shift = 43
        elif shift == 'r':
            shift = 44
        elif shift == 's':
            shift = 45
        elif shift == 't':
            shift = 46
        elif shift == 'u':
            shift = 47
        elif shift == 'v':
            shift = 48
        elif shift == 'w':
            shift = 49
        elif shift == 'x':
            shift = 50
        elif shift == 'y':
            shift = 51
        elif shift == 'z':
            shift = 52
        else:
            shift = shift

        mod = 0
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        for char in uppercase_letters:
            if char == "A":
                mod = (1 + shift) % 52
                dictionary_of_shifts['A'] = mod
            elif char == "B":
                mod = (2 + shift) % 52
                dictionary_of_shifts['B'] = mod
            elif char == "C":
                mod = (3 + shift) % 52
                dictionary_of_shifts['C'] = mod
            elif char == "D":
                mod = (4 + shift) % 52
                dictionary_of_shifts['D'] = mod
            elif char == "E":
                mod = (5 + shift) % 52
                dictionary_of_shifts['E'] = mod
            elif char == "F":
                mod = (6 + shift) % 52
                dictionary_of_shifts['F'] = mod
            elif char == "G":
                mod = (7 + shift) % 52
                dictionary_of_shifts['G'] = mod
            elif char == "H":
                mod = (8 + shift) % 52
                dictionary_of_shifts['H'] = mod
            elif char == "I":
                mod = (9 + shift) % 52
                dictionary_of_shifts['I'] = mod
            elif char == "J":
                mod = (10 + shift) % 52
                dictionary_of_shifts['J'] = mod
            elif char == "K":
                mod = (11 + shift) % 52
                dictionary_of_shifts['K'] = mod
            elif char == "L":
                mod = (12 + shift) % 52
                dictionary_of_shifts['L'] = mod
            elif char == "M":
                mod = (13 + shift) % 52
                dictionary_of_shifts['M'] = mod
            elif char == "N":
                mod = (14 + shift) % 52
                dictionary_of_shifts['N'] = mod
            elif char == "O":
                mod = (15 + shift) % 52
                dictionary_of_shifts['O'] = mod
            elif char == "P":
                mod = (16 + shift) % 52
                dictionary_of_shifts['P'] = mod
            elif char == "Q":
                mod = (17 + shift) % 52
                dictionary_of_shifts['Q'] = mod
            elif char == "R":
                mod = (18 + shift) % 52
                dictionary_of_shifts['R'] = mod
            elif char == "S":
                mod = (19 + shift) % 52
                dictionary_of_shifts['S'] = mod
            elif char == "T":
                mod = (20 + shift) % 52
                dictionary_of_shifts['T'] = mod
            elif char == "U":
                mod = (21 + shift) % 52
                dictionary_of_shifts['U'] = mod
            elif char == "V":
                mod = (22 + shift) % 52
                dictionary_of_shifts['V'] = mod
            elif char == "W":
                mod = (23 + shift) % 52
                dictionary_of_shifts['W'] = mod
            elif char == "X":
                mod = (24 + shift) % 52
                dictionary_of_shifts['X'] = mod
            elif char == "Y":
                mod = (25 + shift) % 52
                dictionary_of_shifts['Y'] = mod
            elif char == "Z":
                mod = (26 + shift) % 52
                dictionary_of_shifts['Z'] = mod
        for char in lowercase_letters:
            if char == "a":
                mod = (27 + shift) % 52
                dictionary_of_shifts['a'] = mod
            elif char == "b":
                mod = (28 + shift) % 52
                dictionary_of_shifts['b'] = mod
            elif char == "c":
                mod = (29 + shift) % 52
                dictionary_of_shifts['c'] = mod
            elif char == "d":
                mod = (30 + shift) % 52
                dictionary_of_shifts['d'] = mod
            elif char == "e":
                mod = (31 + shift) % 52
                dictionary_of_shifts['e'] = mod
            elif char == "f":
                mod = (32 + shift) % 52
                dictionary_of_shifts['f'] = mod
            elif char == "g":
                mod = (33 + shift) % 52
                dictionary_of_shifts['g'] = mod
            elif char == "h":
                mod = (34 + shift) % 52
                dictionary_of_shifts['h'] = mod
            elif char == "i":
                mod = (35 + shift) % 52
                dictionary_of_shifts['i'] = mod
            elif char == "j":
                mod = (36 + shift) % 52
                dictionary_of_shifts['j'] = mod
            elif char == "k":
                mod = (37 + shift) % 52
                dictionary_of_shifts['k'] = mod
            elif char == "l":
                mod = (38 + shift) % 52
                dictionary_of_shifts['l'] = mod
            elif char == "m":
                mod = (39 + shift) % 52
                dictionary_of_shifts['m'] = mod
            elif char == "n":
                mod = (40 + shift) % 52
                dictionary_of_shifts['n'] = mod
            elif char == "o":
                mod = (41 + shift) % 52
                dictionary_of_shifts['o'] = mod
            elif char == "p":
                mod = (42 + shift) % 52
                dictionary_of_shifts['p'] = mod
            elif char == "q":
                mod = (43 + shift) % 52
                dictionary_of_shifts['q'] = mod
            elif char == "r":
                mod = (44 + shift) % 52
                dictionary_of_shifts['r'] = mod
            elif char == "s":
                mod = (45 + shift) % 52
                dictionary_of_shifts['s'] = mod
            elif char == "t":
                mod = (46 + shift) % 52
                dictionary_of_shifts['t'] = mod
            elif char == "u":
                mod = (47 + shift) % 52
                dictionary_of_shifts['u'] = mod
            elif char == "v":
                mod = (48 + shift) % 52
                dictionary_of_shifts['v'] = mod
            elif char == "w":
                mod = (49 + shift) % 52
                dictionary_of_shifts['w'] = mod
            elif char == "x":
                mod = (50 + shift) % 52
                dictionary_of_shifts['x'] = mod
            elif char == "y":
                mod = (51 + shift) % 52
                dictionary_of_shifts['y'] = mod
            elif char == "z":
                mod = (52 + shift) % 52
                dictionary_of_shifts['z'] = mod
            else:
                print("Error")
                
        for key in dictionary_of_shifts:
 #           print(key, dictionary_of_shifts[key])
            if dictionary_of_shifts[key] == 0:
                dictionary_of_shifts[key] == "Z"
            elif dictionary_of_shifts[key] == 1:
                dictionary_of_shifts[key] = "A"
            elif dictionary_of_shifts[key] == 2:
                dictionary_of_shifts[key] = "B"
            elif dictionary_of_shifts[key] == 3:
                dictionary_of_shifts[key] = "C"
            elif dictionary_of_shifts[key] == 4:
                dictionary_of_shifts[key] = "D"
            elif dictionary_of_shifts[key] == 5:
                dictionary_of_shifts[key] = "E"
            elif dictionary_of_shifts[key] == 6:
                dictionary_of_shifts[key] = "F"
            elif dictionary_of_shifts[key] == 7:
                dictionary_of_shifts[key] = "G"
            elif dictionary_of_shifts[key] == 8:
                dictionary_of_shifts[key] = "H"
            elif dictionary_of_shifts[key] == 9:
                dictionary_of_shifts[key] = "I"
            elif dictionary_of_shifts[key] == 10:
                dictionary_of_shifts[key] = "J"
            elif dictionary_of_shifts[key] == 11:
                dictionary_of_shifts[key] = "K"
            elif dictionary_of_shifts[key] == 12:
                dictionary_of_shifts[key] = "L"
            elif dictionary_of_shifts[key] == 13:
                dictionary_of_shifts[key] = "M"
            elif dictionary_of_shifts[key] == 14:
                dictionary_of_shifts[key] = "N"
            elif dictionary_of_shifts[key] == 15:
                dictionary_of_shifts[key] = "O"
            elif dictionary_of_shifts[key] == 16:
                dictionary_of_shifts[key] = "P"
            elif dictionary_of_shifts[key] == 17:
                dictionary_of_shifts[key] = "Q"
            elif dictionary_of_shifts[key] == 18:
                dictionary_of_shifts[key] = "R"
            elif dictionary_of_shifts[key] == 19:
                dictionary_of_shifts[key] = "S"
            elif dictionary_of_shifts[key] == 20:
                dictionary_of_shifts[key] = "T"
            elif dictionary_of_shifts[key] == 21:
                dictionary_of_shifts[key] = "U"
            elif dictionary_of_shifts[key] == 22:
                dictionary_of_shifts[key] = "V"
            elif dictionary_of_shifts[key] == 23:
                dictionary_of_shifts[key] = "W"
            elif dictionary_of_shifts[key] == 24:
                dictionary_of_shifts[key] = "X"
            elif dictionary_of_shifts[key] == 25:
                dictionary_of_shifts[key] = "Y"
            elif dictionary_of_shifts[key] == 26:
                dictionary_of_shifts[key] = "Z"
            elif dictionary_of_shifts[key] == 27:
                dictionary_of_shifts[key] = "a"
            elif dictionary_of_shifts[key] == 28:
                dictionary_of_shifts[key] = "b"
            elif dictionary_of_shifts[key] == 29:
                dictionary_of_shifts[key] = "c"
            elif dictionary_of_shifts[key] == 30:
                dictionary_of_shifts[key] = "d"
            elif dictionary_of_shifts[key] == 31:
                dictionary_of_shifts[key] = "e"
            elif dictionary_of_shifts[key] == 32:
                dictionary_of_shifts[key] = "f"
            elif dictionary_of_shifts[key] == 33:
                dictionary_of_shifts[key] = "g"
            elif dictionary_of_shifts[key] == 34:
                dictionary_of_shifts[key] = "h"
            elif dictionary_of_shifts[key] == 35:
                dictionary_of_shifts[key] = "i"
            elif dictionary_of_shifts[key] == 36:
                dictionary_of_shifts[key] = "j"
            elif dictionary_of_shifts[key] == 37:
                dictionary_of_shifts[key] = "k"
            elif dictionary_of_shifts[key] == 38:
                dictionary_of_shifts[key] = "l"
            elif dictionary_of_shifts[key] == 39:
                dictionary_of_shifts[key] = "m"
            elif dictionary_of_shifts[key] == 40:
                dictionary_of_shifts[key] = "n"
            elif dictionary_of_shifts[key] == 41:
                dictionary_of_shifts[key] = "o"
            elif dictionary_of_shifts[key] == 42:
                dictionary_of_shifts[key] = "p"
            elif dictionary_of_shifts[key] == 43:
                dictionary_of_shifts[key] = "q"
            elif dictionary_of_shifts[key] == 44:
                dictionary_of_shifts[key] = "r"
            elif dictionary_of_shifts[key] == 45:
                dictionary_of_shifts[key] = "s"
            elif dictionary_of_shifts[key] == 46:
                dictionary_of_shifts[key] = "t"
            elif dictionary_of_shifts[key] == 47:
                dictionary_of_shifts[key] = "u"
            elif dictionary_of_shifts[key] == 48:
                dictionary_of_shifts[key] = "v"
            elif dictionary_of_shifts[key] == 49:
                dictionary_of_shifts[key] = "w"
            elif dictionary_of_shifts[key] == 50:
                dictionary_of_shifts[key] = "x"
            elif dictionary_of_shifts[key] == 51:
                dictionary_of_shifts[key] = "y"
            elif dictionary_of_shifts[key] == 52:
                dictionary_of_shifts[key] = "z"


        return dictionary_of_shifts
                

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        letters = self.build_shift_dict(shift)
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
 #       print(letters.keys())
        for char in self.message_text:
            if char not in uppercase_letters and char not in lowercase_letters:
                continue
            if char in letters.keys() and type(char) != int():
                self.message_text = self.message_text.replace(str(char), str(letters[char]))
            else:
                continue
        return self.message_text

class PlaintextMessage(Message):
    def __init__(self, message_text, shift, valid_words="", encrypting_dict="", message_text_encrypted=""):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = message_text
        self.shift = shift
        self.valid_words = valid_words
        self.encrypting_dict = encrypting_dict
        self.message_text_encrypted = message_text_encrypted

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        self.encrypting_dict = Message(self.message_text, self.shift).build_shift_dict(self.shift)
        return self.encrypting_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return Message(self.message_text).apply_shift(self.shift)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        


class CiphertextMessage(Message):
    def __init__(self, text, wordlist):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text
        self.valid_words = wordlist
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        new_word = []
        all_dicts = []
        string = ""
        for char in self.text:
            for x in range(1, 52):
                all_dicts.append(dict(Message(self.text).build_shift_dict(x)))
        for val in all_dicts:
            for char in self.text:
                string += str(val.get(char))
            new_word.append(str(string))
            string = ""
        for word in new_word:
            if is_word(self.valid_words, word):
                return word

                
#        print(new_word)

#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello', 2)
wordlist = load_words('./words.txt')
plaintext = PlaintextMessage('charles', 13)
print('Encrypted Output:', plaintext.get_message_text_encrypted())
plaintext = PlaintextMessage('truscott', 1)
print('Encrypted Output:', plaintext.get_message_text_encrypted())
plaintext = PlaintextMessage('watters', 93)
print('Encrypted Output:', plaintext.get_message_text_encrypted())
#print('Expected Output: jgnnq')
#print(Message("foo").build_shift_dict(16))   
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('punEyrF', wordlist)
ciphertext.decrypt_message()
print('Decrypted Output:', ciphertext.decrypt_message())
ciphertext = CiphertextMessage('vuvudpvv', wordlist)
ciphertext.decrypt_message()
print('Decrypted Output:', ciphertext.decrypt_message())
ciphertext = CiphertextMessage('lPiiTgh', wordlist)
ciphertext.decrypt_message()
print('Decrypted Output:', ciphertext.decrypt_message())
#print('Expected Output:', (24, 'hello'))

