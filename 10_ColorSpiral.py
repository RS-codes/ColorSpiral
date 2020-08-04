#10_ColorSpiral.py -No of sides in our Spiral shape
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#You can choose between 2 and 6 sides for some cool shapes!
sides = 6
colors = ["red", "yellow", "blue", "pink", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)  #changes width of turtle pen

#FunTips:
#Change no. of sides from 5,3,2,1 and have fun :)