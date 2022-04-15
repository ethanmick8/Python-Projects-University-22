# Author: Ethan Mick
# Instructor: Dale Musser
# Program Explanation: This program outlines a class called "Animal" that holds information for
# the creation and specification of different types of animals and their basic qualities.

from random import randint

class Animal(object):
    def __init__(self, animal_type, name ):
        self.__animal_type = animal_type
        self.__name = name
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

    # setter for the name of the animal
    def set_name( self, __name ):
        self.__name = __name

    # getter("checker") for the mood of the animal. Result is random with 3 possibilities
    def check_mood( self ):
            return self.__mood

# Bird subclass of class Animal; has one additional attribute and method
class Bird(Animal):
    def __init__(self, animal_type, name, can_fly):
        super().__init__(animal_type, name)
        self.__can_fly = can_fly
    
    # getter for whether or not the bird can fly
    def get_can_fly(self):
        return self.__can_fly

# Mammal subclass of class Animal, also has one additional atrribute and method
class Mammal(Animal):
    def __init__(self, animal_type, name, hair_color):
        super().__init__(animal_type, name)
        self.__hair_color = hair_color

    # getter for the hair color of the mammal
    def get_hair_color(self):
        return self.__hair_color
