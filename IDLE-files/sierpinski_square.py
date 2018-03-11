# The Sierpinski square.
# Run the Module (or type F5).

from turtle import *

def sierpinski_square(length, level):
    speed(0) # Fastest speed
    if level==0:
        return
    begin_fill() # Fill shape
    color("red")

    for i in range(4):
        sierpinski_square(length/3, level-1)
        fd(length/2)
        sierpinski_square(length/3, level-1)
        fd(length/1)
        lt(90) # Left turn 90 degrees
    end_fill()
