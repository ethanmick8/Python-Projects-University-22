# Random Write Assignment
# Assigned by: Dale Musser
# Author: Ethan Mick

import math as m
import random as rand

# Function that retrieves quantity of random numbers to be generated from user input
def get_quantity():
    quantity = 0
    while(True):
        try:
            quantity = int( input( "Please indicate the amount of random numbers you would like to generate: " ) )
            if ( quantity <= 0 ):
                print( "Invalid input. Only nonzero positive values are to be accepted." )
                continue
        except:
            print( "Invalid input. Only positive, nonzero, numerical values are to be accepted." )
            continue
        else:
            break
    return quantity

# Function that retrieves the lower bound of random numbers to be generated from user input
def get_lower():
    lower_bound = 0
    while(True):
        try:
            lower_bound = int( input( "Please indicate the lower bound of the random numbers' range: " ) )
            if ( lower_bound <= 0):
                print( "Invalid input. Only nonzero positive values are to be accepted." )
                continue
        except:
            print( "Invalid input. Only positive, nonzero, numerical values are to be accepted." )
            continue
        else:
            break
    return lower_bound

# Function that retrieves the upper bound of random numbers to be generated from user input
def get_upper():
    upper_bound = 0
    while(True):
        try:
            upper_bound = int( input( "Please indicate the upper bound of the random numbers' range: " ) )
            if ( upper_bound <= 0 ):
                print( "Invalid input. Only nonzero positive values are to be accepted." )
                continue
        except:
            print( "Invalid input. Only positive, nonzero, numerical values are to be accepted." )
            continue
        else:
            break
    return upper_bound

# Function that carries out the core task of the program, utilizing passed variables from the previous functions
def write_to_file():
    quantity = get_quantity()
    lower_bound = get_lower()
    upper_bound = get_upper()

    f = open( "randomnum.txt", "w" ) # open the file for writing
    for _ in range(quantity):
        value = rand.randint( lower_bound, upper_bound ) # Specify the range in which to generate random numbers
        f.write( "{:d}\n".format(value, 'd' ) )
    f.close()

# Main Function
def main():
    write_to_file()
    print( "The random numbers were successfully written to the file 'randomnum.txt'." )

# execute main
main()










