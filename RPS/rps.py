# Author: Ethan Mick
# Instructor: Dale Musser
# Description: This is a menu driven rock paper scissors simulator. It allows users to play
# RPS and save their data, or start new games. Data is saved for each data based on their
# name, and players can return to play where they left off whenever they want.

import pickle # for serializing user data
from os import path
import random as rand # computer's choices

# Menu error check
class Error(Exception):
    pass
class OutOfRangeError(Error):
    pass
class rpsError(Error):
    pass

# This function is called by main when a game of rps is commenced; it has its own sub-menu for the
# gameplay and it calls statistics upon request to display to the user their wins/losses etc. THe
# parameter that is passed in is expected to be a list in the order of name, wins, losses, ties and
# the function increments those values accordingly throughout the duration of a game. 
def gameplay(data):
    while(True):
        rounds_played = data[1] + data[2] + data[3] # sum
        print("\nRound {}".format(rounds_played))
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors\n")
        while(True):
            try:
                user_choice = input("What will it be?: ")
                if user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissors":
                    raise rpsError 
                break
            except:
                print("Please enter either Rock, Paper, or Scissors.")

        rps_choices = ["Rock", "Paper", "Scissors"]
        bot_choice = rand.choice(rps_choices)
        if user_choice == bot_choice:
            print("The computer chose {} too! The result is a tie.\n".format(bot_choice))
            data[3] += 1 # increment ties
        elif user_choice == "Rock":
            if bot_choice == "Scissors":
                print("You chose Rock. The computer chose Scissors. Rock crushes Scissors!\n")
                data[1] += 1 # increment wins
            else:
                print("You chose Rock. The computer chose Paper. Paper covers Rock!\n")
                data[2] += 1 # increment losses
        elif user_choice == "Paper":
            if bot_choice == "Rock":
                print("You chose Paper. The computer chose Rock. Paper covers Rock!\n")
                data[1] += 1
            else:
                print("You chose Paper. The computer chose Scissors. Scissors cuts Paper!\n")
                data[2] += 1
        elif user_choice == "Scissors":
            if bot_choice == "Paper":
                print("You chose Scissors. THe computer chose Paper. Scissors cuts Paper!\n")
                data[1] += 1
            else:
                print("You chose Scissors. The computer chose Rock. Rock crushes Scissors!\n")
                data[2] += 1
                    
        while(True):
            print("What would you like to do now?")
            print("\n1. Play Again")
            print("2. View Statistics")
            print("3. Quit Game\n")
            while(True):
                try:
                    choice = int(input("Enter choice: ")) 
                    if choice < 1 or choice > 3:
                        raise OutOfRangeError
                    break
                except:
                    print("Please enter a number from the menu.")

            if choice == 1: # another match
                break 

            if choice == 2: # view current stats
                display_stats(data)
                continue

            if choice == 3: # quit game
                return

# This function displays the statistics of a players rps gameplay history. It expects a list as
# a parameter, and that list is expected to be in the specific order of name, wins, losses, ties.
def display_stats(data):
    print("{}, here are your gameplay statistics...".format(data[0]))
    print("Wins: {}".format(data[1]))
    print("Losses: {}".format(data[2]))
    print("Ties: {}".format(data[3]))
    wlr = float(data[1] / data[2]) # win loss ratio
    print("\nWin/Loss Ratio: {:.2f}".format(wlr))

# This function takes a players data expected to be in the form explained in the display_stats()
# documentation, as well as a filename. THe filename is expected to be the name of the user with
# ".rps" added on to the end. THe function uses the Python pickle module to serialize the passed
# in data into a stream of bytes for later retrieval.
def serialize_data(data, filename):
    try:
        with open(filename, "wb") as outfile:
            pickle.dump(data, outfile) # serialize the data
    except Exception as e:
        print("Sorry {}, the game could not be saved\n")
        print(e)
    return

def main():
    player_data = []
    while(True):
        print("\nWelcome to Rock, Paper, Scissors!")
        print("\n1. Start New Game")
        print("2. Load Game")
        print("3. Quit\n")
        while(True):
            try:
                choice = int(input("Enter choice: ")) 
                if choice < 1 or choice > 3:
                    raise OutOfRangeError
                break
            except:
                print("Please enter a number from the menu.")
    
        if(choice == 1):
            name = input("\nWhat is your name?: ")
            print("Hello {}. Let's play!".format(name))
            player_data.append(name)
            i = 1
            while( i < 4):
                player_data.append(0)
                i += 1
            gameplay(player_data)
            filename = "{}.rps".format(name)
            serialize_data(player_data, filename)

        if(choice == 2):
            name = input("\nWhat is your name?: ")
            filename = "{}.rps".format(name)
            if(path.exists(filename)):
                with open(filename, "rb") as infile:
                    player_data = pickle.load(infile)
                gameplay(player_data)
                serialize_data(player_data, filename)
            else:
                print("{}, your game could not be found.\n".format(name))
                continue

        if(choice == 3):
            break # end the program

main()
