import colorgram
import random
from turtle import *

new_color = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]

b = Turtle()
b.speed("fastest")
b.penup()
b.hideturtle()
colormode(255)
b.setheading(225)
b.forward(300)
b.setheading(0)
dots = 100

for dots_count in range(1, dots + 1):  
    b.dot(20, random.choice(new_color))
    b.forward(50)
    
    if dots_count % 10 == 0:
        b.setheading(90)
        b.forward(50)
        b.setheading(180)
        b.forward(500)
        b.setheading(0)



s = Screen()
s.exitonclick()

