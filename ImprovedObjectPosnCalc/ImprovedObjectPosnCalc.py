print( "Below, you will enter values for the initial position and velocity, as well as the acceleration and time that as passed for an object in motion." )
print( "This program will take what is entered and provide you with the final position of the object." )

# Set up a system of while loops that ensures all possible input errors are accounted for
do_calculation = True # Loop is infinite until do_calculation is False
while ( do_calculation ):
    while( True ):
        try:
            pos_initial = float( input( "Enter the initial position: " ) )
        except:
            print( "You entered an invalid value! Only numerical values are allowed. Please retry." )
        else:
            break
    while( True ):
        try:
            vel_initial = float( input( "Enter the initial velocity: " ) )
        except:
            print( "You entered an invalid value! Only numerical values are allowed. Please retry." )
        else:
            break
    while( True ):
        try:
            acceleration = float( input( "Enter the acceleration: " ) )
        except:
            print( "You enter an invalid value! Only numerical values are allowed. Please retry." )
        else:
            break
    while( True ):
        try:
            time = float( input( "Enter the time that has passed: " ) )
            if( time < 0 ): # Don't allow negative values for time
                print( "Negative values are not allowed for the intial position. Please retry." )
                continue
        except:
            print( "You entered an invalid value! Only positive numerical values are allowed. Please retry." )
        else:
            break
    # Do the calculation
    vel_final = float( pos_initial + vel_initial * time + 0.5 * acceleration * time * time )
    print( "The final velocity is: {:.2f}".format( vel_final ) )
    # Determine if the user wants to perform another calculation
    another_calculation = input( "Would you like to perform another calculation (y/n): ")
    if( another_calculation != "y" ):
        do_calculation = False # Terminate the loop and thus the program
