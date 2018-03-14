# Plot the Koch snowflake.
# See Exercise 1(d).
# Run the Module (or type F5).
from turtle import *

def koch_snowflake(length, level):  # KochSnowflake function.
    speed(0)                      # Fastest speed.
    for i in range(3):
        plot_side(length, level)
        rt(120)

def plot_side(length, level):    # PlotSide function.
    if level==0:
        fd(length)
        return
    plot_side(length/3, level-1)
    lt(60)
    plot_side(length/3, level-1)
    lt(-120)
    plot_side(length/3, level-1)
    lt(60)
    plot_side(length/3, level-1)
