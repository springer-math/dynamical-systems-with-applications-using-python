# Koch square fractal.
# Run the Module (or type F5).
# Save file as koch_square.py.

from turtle import *

def koch_square(length, level):
    speed(0)  # Fastest speed.
    for i in range(4):
        plot_side(length, level)
        rt(90)

def plot_side(length, level):
    if level==0:
        fd(length)
        return
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)
