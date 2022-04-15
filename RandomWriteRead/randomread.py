# Random Read Assignment
# Assigned by: Dale Musser
# Author: Ethan Mick

# Function that reads the numbers from the randomnum.txt file and prints them out
# This function also handles counting the number of numbers in the number file
def readfile():
    counter = 0
    try:
        f = open( "randomnum.txt", "r" )
    except:
        print( "The file could not be opened." )
    else:
        print( "List of random numbers in randomnum.txt:" )
        content = f.read()
        file = content.split( "\n" ) # specify the need to read line by line

        print( content ) # print out the numbers in the file

        # loop through for the entirety of the file in order to determine the number of numbers in the file
        for i in file:
            if i:
                counter += 1
        
        print( "Random number count: {:d}".format(counter, 'd') ) # print out the number of numbers

# Main function; used to run readfile()
def main():
    readfile()

# Run main
main()


