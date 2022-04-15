# Author: Ethan Mick
# Instructor: Dale Musser
# Program Explanation: This program is designed to allow users to create "Animal" objects 
# that hold information about the objects such as name, mood, and type. The user is allowed
# to create as many animals as they would like, and then "getter" functions defined in the
# "Animal" class (see Animals.py) can be used to retrieve specific data regarding the animals

# import my module (Animals.py file containing Animal class) and abbreviate it to "A"
import Animals as A

# This function creates an mammal with the passed in name and type, which in the case of this program 
# will be entered by the user. The function stores the user's data in the Mammal object subclass of 
# class Animal, and returns a string displaying the animal's type, name, and mood
def create_mammal( type, name, hair_color ):
    # create the specified animal using our imported module
    a = A.Mammal( type, name, hair_color )

    # Call our "getter" functions and simultaneously format the data that they return into a
    # string that displays the data
    animal_info = a.get_name() + " the " + a.get_animal_type() + " is " + a.check_mood() + "\n"

    return animal_info # return the data

# This function does the same as the above function, except it creates a Bird with the passed in data.
def create_bird( type, name, can_fly ):
    a = A.Bird( type, name, can_fly )

    animal_info = a.get_name() + " the " + a.get_animal_type() + " is " + a.check_mood() + "\n"

    return animal_info

def main():
    print( "Welcome to the Animal Generator!" )
    print( "This program creates Animal objects.\n" )

    # Initialize a string to hold all the data for the animals the user will create
    animal_data = ""

    # while loop for "Animal" object creation
    while(True):
        # prompt the user as to what kind of animal they would like to create
        print( "Would you like to create a mammal or a bird?:" )
        print( "1. Mammal" )
        print( "2. Bird" )
        mammal_or_bird = input( "Which would you like to create?: " )
        mammal_or_bird = int(mammal_or_bird) # cast input string to int
        if mammal_or_bird == 1:
            # prompt the user for characteristics of the animal
            name = input( "What is the mammal's name?: " )
            type = input( "What type of mammal is it?: " )
            hair_color = input( "What color hair does the mammal have?: " )
            # create the animal, as well as its formatted info string
            fetch_mammal = create_mammal( type, name, hair_color ) 
            # append the newly created animal data to the master list of animal data
            animal_data += fetch_mammal
        elif mammal_or_bird == 2:
            name = input( "What is the birds name?: " )
            type = input( "What type of bird are they?: " )
            can_fly = input( "Can the bird fly(Yes/No)?: " )
            fetch_bird = create_bird( type, name, can_fly )
            animal_data += fetch_bird
        else:
            print( "Error: invalid number entered." )

        # Ask the user if they would like to create another animal
        another_animal = input( "\nWould you like to add more animals(y/n)?: " )
        if ( another_animal != 'y' ):
            print( "\n" )
            break # no further animals
        else:
            print( "\n" )
            continue # another iteration (another animal)

    # Finally, print out the information on all of the animals that the user created
    print( "Animal List:" )
    print( animal_data )

main()
