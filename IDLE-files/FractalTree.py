# A fracta tree.

from turtle import *
setheading(90)   # The turtle points straight up.

def FractalTree(length, level): # Fractal tree function.
    """
    Draws a fractal tree
    """
    speed(0)         # The fastest speed.
    if level > 0:
        fd(length)   # Forward.
        rt(30)       # Right turn.
        FractalTree(length*0.7, level-1)
        lt(90)       # Left turn.
        FractalTree(length*0.5, level-1)
        rt(60)       # Rotate 60 degrees.
        bk(length)   # Back.

