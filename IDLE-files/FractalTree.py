from turtle import *
def FractalTree(length, level):
    """
    Draws a fractal tree
    """
    speed(0)
    if level > 0:
        fd(length)
        rt(30)
        FractalTree(length*0.7, level-1)
        lt(90)
        FractalTree(length*0.5, level-1)
        rt(60)
        bk(length)

