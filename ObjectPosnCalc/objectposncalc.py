print( "Below, you will enter values for the initial position and velocity, as well as the acceleration and time that as passed for an object in motion." )
print( "This program will take what is entered and provide you with the final position of the object." )
pos_initial = float( input( "Enter the initial position: " ) )
vel_initial = float( input( "Enter the initial velocity: " ) )
acceleration = float( input( "Enter the acceleration: " ) )
time = float( input( "Enter the time that has passed: " ) )
vel_final = float( pos_initial + vel_initial * time + 0.5 * acceleration * time * time )
print( "The final velocity is: {:.2f}".format( vel_final ) )
