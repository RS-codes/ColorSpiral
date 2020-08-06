#11_ColorSpiral2.py - version 2 - more sides & colors
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 8 #change it to 10 and add colors, later and observe
colors = ["red", "yellow", "crimson", "blue", "orange", "green", "purple", "cyan"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)