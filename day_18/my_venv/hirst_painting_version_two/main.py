import colorgram
from turtle import *
import random

colors = [(203, 172, 107), (153, 181, 196), (193, 161, 177), (152, 186, 174), (214, 204, 111), (208, 179, 196), (174, 189, 213), (161, 203, 216), (160, 214, 187), (114, 123, 186), (178, 161, 71), (213, 182, 180), (98, 98, 97), (41, 41, 41), (94, 92, 93), (201, 207, 43), (53, 51, 52), (130, 127, 128), (105, 105, 107), (66, 63, 64)]

# Create a turtle method
b = Turtle()

b.speed('fastest')
b.penup()
b.hideturtle()
colormode(255)
b.setheading(225)
b.forward(500)
b.setheading(0)
number_dot = 150



for dots_count in range(1, number_dot + 1):
    b.dot(40, random.choice(colors))
    b.forward(50)
    
    if dots_count % 10 == 0:
        b.setheading(90)
        b.forward(50)
        b.setheading(180)
        b.forward(500)
        b.setheading(0)


s = Screen()
s.exitonclick()