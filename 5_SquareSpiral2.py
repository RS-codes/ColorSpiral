#5_SquareSpiral2 - version2
import turtle
t = turtle.Pen()
for x in range (100):
    t.forward(x)
    t.left(91)      #not a perfect square-looks more of a staircase

#FunTips:
#Change the number of lines the program draws to 200, or 500,
#or 50, by changing the value in parentheses after range .
#Also try changing the angle in the last line to 91, 46, 61, or
#121, and so on.