#4_SquareSpiral.py - Draws a square spiral
import turtle       #library
t = turtle.Pen()    #short-hand
for x in range(100): #loop to draw
    t.forward(x)    #move forward x dots
    t.left(90)      #turn left by angle
