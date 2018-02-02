from turtle import *
def KochSquare(length, level):  # KochSquare function.
    speed(0)                    # Fastest spped.
    for i in range(4):
        PlotSide(length, level)
        rt(90)

def PlotSide(length, level):    # PlotSide function.
    if level==0:
        fd(length)
        return
    PlotSide(length/3,level-1)
    lt(90)
    PlotSide(length/3,level-1)
    rt(90)
    PlotSide(length/3,level-1)
    rt(90)
    PlotSide(length/3,level-1)
    lt(90)
    PlotSide(length/3,level-1)
    


