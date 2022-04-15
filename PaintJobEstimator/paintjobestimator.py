print( "Welcome to the paint job estimator." )

# import the math module and abbreviate it to m. I'm doing this so that I can
# have access to the ceil() function to make it easy to round later on.
import math as m

do_calc = True
while( do_calc ):

    # print a spacer to increase visual appeal
    print( "--------------------------------------------------------------")

    # Obtain user input for the square feet and price per gallon, making sure to error check for invalid inputs
    while( True ):
        try:
            sqft = float( input( "Please enter the square feet of wall space to be painted: " ) )
            if( sqft <= 0 ): # error check
                print( "You entered an invalid value! Only positive nonzero rational numbers are allowed. Please retry." )
                continue
        except:
            print( "You entered an invalid value! Only positive nonzero rational numbers are allowed. Please retry." )
        else:
            break
    while( True ):
        try:
            ppgallon = float( input( "Please enter the price per gallon in dollars: " ) )
            if ( ppgallon <= 0 ): # error check
                print( "You entered an invalid value! Only positive nonzero rational numbers are allowed. Please retry." )
                continue
        except:
            print( "You entered an invalid value! Only positive nonzero rational numbers are allowed. Please retry." )
        else:
            break
    
    # perform calculations using user-entered & pre-determined values, making sure to round when required
    ReqGallons = int( m.ceil( sqft / 350 ) )
    HoursLabor = float( 6 * ( sqft / 350 ) )
    CostOfPaint = float( ReqGallons * ppgallon )
    LaborCharges = float( 62.25 * HoursLabor )
    TotalCost = CostOfPaint + LaborCharges

    # spacer
    print( "-------------------------------------------------------------" )

    # display calculated job information
    print( "The number of gallons of paint required for this job is: {:d}".format( ReqGallons ) )
    print( "Hours of labor required: {:.1f}".format( HoursLabor ) )
    print( "Cost of the paint: ${:.2f}".format( CostOfPaint ) )
    print( "Labor charges: ${:.2f}".format( LaborCharges ) )
    print( "Total cost of paint job: ${:.2f}".format( TotalCost ) )

    # spacer
    print( "-------------------------------------------------------------" )

    # Now, determine if the user wants to do another calculation
    another_calc = input( "Would you like to do another estimate? (y/n): " )
    if( another_calc != "y" ):
        do_calc = False # Terminate loop and end the porgram
    # otherwise, the loop will start again from the top