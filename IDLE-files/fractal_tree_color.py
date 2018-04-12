# A program to plot a color fractal tree.
# Run Module and type >>> fractal_tree_color(200, 10) in the Python Shell.

from turtle import *

setheading(90)  # The turtle points straight up
penup()  # Lift the pen
setpos(0, -250)  # Set initial point
pendown()  # Pen down

def fractal_tree_color(length, level):
    """
    Draws a fractal tree
    """
    pensize(length/10)       # Thickness of lines.
    if length < 20:
        pencolor("green")
    else:
        pencolor("brown")

    speed(0)
    if level > 0:
        fd(length)  # Forward
        rt(30)  # Right turn 30 degrees
        fractal_tree_color(length*0.7, level-1)
        lt(90)  # Left turn 90 degrees
        fractal_tree_color(length*0.5, level-1)
        rt(60)  # Right turn 60 degrees
        penup()
        bk(length)  # Backward
        pendown()
