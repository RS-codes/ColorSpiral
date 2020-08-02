#8_ColorSquareSpiral.py - A Four-Color Spiral
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]  #List
for x in range(100):
    t.pencolor(colors[x%4]) #rotate through a certain number of items in alist, like we’re doing with our list of four colors
                            #0%4=0, 1%4=0..5%4=1,6%4=2
    t.forward(x)
    t.left(91)