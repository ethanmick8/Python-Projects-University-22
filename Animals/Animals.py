# Author: Ethan Mick
# Instructor: Dale Musser
# Program Explanation: This program outlines a class called "Animal" that holds information for
# the creation and specification of different types of animals and their basic qualities.

from random import randint

class Animal:
    def __init__(self, __animal_type, __name ):
        self.set_animal_type( __animal_type )
        self.set_name( __name )
        mood_indicator = randint( 1, 3 ) # generate a random number between 1 and 3
        if( mood_indicator == 1 ):
            self.__mood = "happy"
        elif( mood_indicator == 2 ):
            self.__mood = "hungry"
        elif( mood_indicator == 3 ):
            self.__mood = "sleepy"

    # getter for the animal type
    def get_animal_type( self ):
        return self.__animal_type

    # getter for the name of the animal
    def get_name( self ):
        return self.__name

    # getter("checker") for the mood of the animal. Result is random with 3 possibilities
    def check_mood( self ):
            return self.__mood

    # setter for the animal type
    def set_animal_type( self, __animal_type ):
        self.__animal_type = __animal_type

    # setter for the name of the animal
    def set_name( self, __name ):
        self.__name = __name

    