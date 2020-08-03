#8_ColorCircleSpiral.py - A Four-Color Spiral with black Background
import turtle
t = turtle.Pen()
turtle.bgcolor("black") #choose any Background color
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)