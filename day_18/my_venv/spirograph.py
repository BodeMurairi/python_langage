from turtle import *
import random

b = Turtle()

direction = [0,30,60,90,120, 150, 180,210,240,270, 300, 330,360]
color_choice = ["blue", "orange red", "yellow", "dark orange", "green", "medium spring green"]

def spirograph(side_number):
    for _ in range(int(360 / side_number)):
        b.color(random.choice(color_choice))
        b.setheading(random.choice(direction))
        b.circle(50, 360)

spirograph(5)

s = Screen()
s.exitonclick()