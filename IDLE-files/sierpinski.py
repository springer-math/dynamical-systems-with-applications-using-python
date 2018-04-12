# Sierpinski triangle.
# Run the Module (or type F5).
# Save the file as sierpinski.py.

from turtle import *

def sierpinski(length, level):
    speed(0)  # Fastest speed.
    if level==0:
        return
    begin_fill()  # Fill shape.
    color('red'sierpinski(200,3))

    for i in range(3):
        sierpinski(length/2,level-1)
        fd(length)
        lt(120)  # Left turn 120 degrees.
    end_fill()
