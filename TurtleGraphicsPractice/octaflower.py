# octaflower.py
# This program uses recursion and Turtle Graphics to create an octagon flower
# Author: Ethan Mick

import turtle
color_master = -1  # Global variable for use in octaflower function

# This function uses python turtle graphics and recursion to create a colored flower-like design
# using octagons. It recurs until the final passed in parameter is equal to 0
def octaflower(turtle, angle, length, axis, x, y, recur):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet" ] # Roy G. Biv
    global color_master
    color_master += 1 # increment global
    if color_master == 7: # if global is out of range for "colors", reset
        color_master = 0
    color = colors[color_master] # retrieve the color based on color_master
    turtle.penup()
    turtle.color(color) # assign color
    turtle.pensize(10)
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.left(axis) # tilt the petal iteration to the left
    # create a pattern of 8 octagons around an axis
    for i in range(8):
        turtle.left(angle)
        for i in range(8):
            turtle.forward(length)
            turtle.left(angle)
    recur = recur - 1 # decrement loop
    if recur > 0:
        octaflower(turtle, angle, length - 2, axis + 67.5, x, y, recur) # recur with new orientation

def main():
    turtle.bgcolor("Black") # looks better
    instance = turtle.Turtle()
    instance.speed(0)
    octaflower(instance, 45, 100, 0, 0, 0, 24) # I did 24 so it would end on yellow; any multiple of 7
    # minus 4 would suffice for this though and probably lower the amnt of time considerably (not as cool though)
    input("Press any key to exit...") # Used to test in VScode

main()