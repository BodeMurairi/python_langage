from turtle import Turtle, Screen
import random

b = Turtle()

side = int(input("Enter the number of side"))

color_choice = ["blue", "orange red", "yellow", "dark orange", "green", "medium spring green"]


def shape(side):
    for _ in range(side):   
        angle = 360 / side
        b.color(random.choice(color_choice))
        b.forward(100)
        b.left(angle)


for _ in range(2, 16):
    shape(_)
    


s = Screen()
s.exitonclick()