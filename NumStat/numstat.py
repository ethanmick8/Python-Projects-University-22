from fileinput import filename
import math as m

# This function retrieves the name of the file  the user is accessing and prints
# it out
def get_filename( file ):     
    print( "'Name of the File: ", file.name )
    print( "\n" ) # Move to next line

# This function gets the count of the numbers in the file and returns that number
def get_count( file ):
    Count = file.read() 
    Lines = Count.split( "\n" ) # This will allow reading of all lines in the file

    # Loop through the file, adding 1 to Count for each line
    for i in Lines:
        if i:
            Count += 1
    
    return Count # return the count

# This function gets the total sum of the numbers in the file and returns that number
def get_sum( file ):
    total = 0 # Initialize total
    try:
        Lines = file.read()
        sum( int(num) for num in Lines.split('\n') ) # sum all the lines in the file
    except ValueError:
        print( '{} is not a number!'.format(Lines) )
        
    return total # return the summed total

# This function takes parameters for the sum of the numbers and the count of the numbers,
# and calculates the average accordingly. It then returns the calculated average
def get_average( Count, Sum ):
    Average = Sum / Count
    return Average

# This function finds the maximum value in the file and returns that number
def get_maximum( file ):
    list = []
    for line in file.readlines():
        list.append(int((line.split('\n'))[0]))
    
    return max(list) # return the max value

# This function finds the minimum value in the file and returns that number
def get_minimum( file ):
    list = []
    for line in file.readlines():
        list.append(int((line.split('\n'))[0]))

    return min(list) # return the min value

# This function finds the range of the numbers in the file. It takes the max and min values
# as parameters and uses them to calculate and return the range.
def get_range( Max, Min ):
    Range = Max - Min
    return Range

# This function takes as parameters all statistics calculated with the other subordinate
# functions in this program and generates a report of the data.
def generate_report( Count, Sum, Average, Max, Min, Range ):
    print( "Sum: ", Sum )
    print( "Count: ", Count )
    print( "Average: ", Average )
    print( "Maximum: ", Max )
    print( "Minimum: ", Min )
    print( "Range: ", Range )

def main():
    do_calculation = True
    print( 'Welcome to the Number Statistics File Reader Program!\n')
    while(do_calculation):
        try:
            ifilename = input( "Please enter the name of the file: " )
            file = open( ifilename, "r" ) # I was having trouble here, for some reason
            # I could not get it to open the file no matter what I tried. To my knowledge,
            # both the file and the program are in the same directory so I don't know why
            # that would be the problem. Maybe I'm just doing something else wrong, 
            # but if I am I don't know what.

            if( file == True ):
                get_filename( file ) # This will just print the filename
                Count = get_count( file )
                Sum = get_sum( file )
                Average = get_average( Count, Sum )
                Max = get_maximum( file )
                Min = get_minimum( file )
                Range = get_range( Max, Min )

                generate_report( Count, Sum, Average, Max, Min, Range )
            
                file.close()
        except IOError:
            print( "\nThe file could not be opened.\n" )

        # Check to see if the user wants to generate another report    
        AnotherRead = input( "Would you like to evaluate another file (y/n)?: " )
        if( AnotherRead != "y" ):
            do_calculation = False

main() # run the program
       




