from turtle import *

bode = Turtle()

for i in range(4):
    bode.forward(100)
    bode.left(90)

for j in range(4):
    bode.forward(100)
    bode.right(90)


screen = Screen()
screen.exitonclick()