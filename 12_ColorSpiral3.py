#12_ColorSpiral3.py - version 3 - user inputs sides
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = eval(input("Enter no.of sides between 3 to 6: "))
colors = ["red", "yellow", "crimson", "blue", "green", "purple", "cyan", "orange"]
for x in range(10):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)