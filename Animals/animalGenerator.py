# Author: Ethan Mick
# Instructor: Dale Musser
# Program Explanation: This program is designed to allow users to create "Animal" objects 
# that hold information about the objects such as name, mood, and type. The user is allowed
# to create as many animals as they would like, and then "getter" functions defined in the
# "Animal" class (see Animals.py) can be used to retrieve specific data regarding the animals

# import my module (Animals.py file containing Animal class) and abbreviate it to "A"
import Animals as A

# This function creates an Animal with the passed in name and type for the Animal, which in the
# case of this program will be entered by the user. The function stores the user's data in the
# Animal object.
def create_animal( type, name ):
    # create the specified animal using our imported module
    a = A.Animal( type, name )

    # Call our "getter" functions and simultaneously format the data that they return into a
    # string that displays the data
    animal_info = a.get_name() + " the " + a.get_animal_type() + " is " + a.check_mood() + "\n"

    return animal_info # return the data

def main():
    print( "Welcome to the Animal Generator!" )
    print( "This program creates Animal objects.\n" )

    # Initialize a string to hold all the data for the animals the user will create
    animal_data = ""

    # while loop for "Animal" object creation
    while(True):
        # prompt the user to enter the type and name of the animal the wish to create
        type = input( "What type of animal would you like to create?: " )
        name = input( "What is the animal's name?: " )
        
        # create the animal, as well as its formatted info string
        fetch_animal = create_animal( type, name ) 

        # append the newly created animal data to the master list of animal data
        animal_data += fetch_animal 

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






