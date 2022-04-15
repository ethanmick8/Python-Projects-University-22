# Program Name: Secret Message Encoder/Decoder
# Author: Ethan Mick
# Instructor: Dale Musser
# Description: This program takes a string and converts it to another string through the use of a cipher. It
# allows the user to do basic encoding and decoding of messages to either hide of reveal their true meaning.
# The cipher being used in this program does have limitations, such as the fact that it does not account for
# upper case characters, numbers, or symbols. The cipher only encodes lowercase characters from the alphabet,
# and decodes a specified selection of numbers/symbols back into their respective lowercase cipher counterparts.

# for this program, I wanted to practice creating my own errors so for the user input in main I used a try/except
# and the custom error class below
class Error(Exception): # base class used for my custom exception
    pass

class OutOfRangeError(Error): # custom exception; raised when user inputs an out of range integer in main
    pass

# This function defines the cipher substitutions with two strings, and replaces all instances of characters in
# the alphabet string with characters in the key string. If a character isn't present in the alphabet string, that
# character remains in the resulting string.
def encode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "0123456789!@#$%^&*()_+<>?="
    print("The encoded message is:","".join([key[alphabet.find(x)] if x in alphabet else x for x in string]))

# This function does essentially the same thing as encode(), except it reverses the conversion to change characters
# from the kye string back into characters from the alphabet string
def decode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "0123456789!@#$%^&*()_+<>?="
    print("The decoded message is:","".join([alphabet[key.find(x)] if x in key else x for x in string]))


# the main function holds the loop that prompts the user for what the want to do. The loop
# continues to iterate after the user chooses to either encode or decode. Once the user chooses
# to exit the program, the loop stops and the program ends.
def main():
    while(True):
        print("\nWelcome to the Secret Message Encoder/Decoder!")
        print("1: Encode a message")
        print("2: Decode a message")
        print("3: Exit")
        try:
            choice = int(input("\nWhat would you like to do?: "))
            if choice < 1 or choice > 3:
                raise OutOfRangeError # integer is not 1, 2, or 3
        except: # this also catches the potentional ValueError (non-integer inputted)
            print("Only the integer values 1, 2, or 3 are expected. Restarting...")
            continue

        if choice == 1: # encode
            message = input("Enter a message to encode: ")
            encode(message)
            continue

        if choice == 2: # decode
            message = input("Enter a message to decode: ")
            decode(message)
            continue

        if choice == 3: # exit program
            break

main()
