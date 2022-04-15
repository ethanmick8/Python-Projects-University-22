# Assignment: Gradebook Challenge
# Author: Ethan Mick
# Instructor: Dale Musser

# Display the average of each student's grade.
# Display the average for each assignment.



# Thid function is designed to go through the 2D array, taking the value at each index
# j column and adding it to the variable x for each i row. It is structured so that it works
# through one row at a time, because a row is considered to be a student in the gradebook
# and that's what we're looking to calculate the average for here.
def print_student_averages( gradebook ):
    print( "Student Averages:" )
    for i in range( len( gradebook ) ):
        sum = 0
        for j in range( len( gradebook[0] ) ):
            sum += gradebook[i][j]
        print( "Student {:}: {:.2f}".format( i+1, sum/(len(gradebook[0]))))

# This function works similar to the print_student_averages function, except [i] and [j] are
# swapped so that the loops consider all values in the column when adding to the sum variable x
# and then dividing by the length, because columns represent individual assignments in the gradebook.
def print_assignment_averages( gradebook ):
    print( "Assignment Averages:" )
    for i in range( len( gradebook[0] ) ):
        sum = 0
        for j in range( len( gradebook ) ):
            sum += gradebook[j][i]
        print( "Assignment {:}: {:.2f}".format( i+1, sum/(len(gradebook))))

def main():
    gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

    # Call functions to print out the data for this gradebook
    print_assignment_averages( gradebook ) 
    print (" ") # spacer
    print_student_averages( gradebook )
    
main()



