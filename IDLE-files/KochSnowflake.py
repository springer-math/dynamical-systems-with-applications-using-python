# Plot the Koch snowflake.
# See Exercise 1(d).
# Run the Module (or type F5). 
from turtle import *
def KochSnowflake(length, level):  # KochSnowflake function.
    speed(0)                      # Fastest speed.
    for i in range(3):
        PlotSide(length, level)
        rt(120)

def PlotSide(length, level):    # PlotSide function.
    if level==0:
        fd(length)
        return
    PlotSide(length/3,level-1)
    lt(60)
    PlotSide(length/3,level-1)
    lt(-120)
    PlotSide(length/3,level-1)
    lt(60)
    PlotSide(length/3,level-1)
    
    


