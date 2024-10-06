from turtle import *
import random

b = Turtle()

path_choice = [0, 90, 120, 270]
color_choice = ["blue", "orange red", "yellow", "dark orange", "green", "medium spring green"]

for i in range(500):
    b.color(random.choice(color_choice))
    b.speed(6)
    b.setheading(random.choice(path_choice))
    b.forward(30)
    b.pensize(10)
    
  #  b.right(path_choice)


s = Screen()
s.exitonclick()