from turtle import Turtle, Screen
import random

screen = Screen()
screen.textinput(title="Make your bet", prompt="Which turtle is going to win? Choose a color? Choose between Red, Blue, Green and Orange ")

screen.setup(width=500, height=400)
colors = ["green", "blue", "red", "orange"]

tim = Turtle("turtle")
tom = Turtle("turtle")
ben = Turtle("turtle")
arnold = Turtle("turtle")

tim.penup()
tim.goto(-250, 0)
tim.color('red')
tom.penup()
tom.goto(-250, 75)
tom.color('blue')
ben.penup()
ben.goto(-250, -75)
ben.color('green')
arnold.color('orange')
arnold.penup()
arnold.goto(-250, 25)

# Setting the turtle speed
speed = random.randint(2, 8)

on_race = True
finish_line = 250  # Adjust this value as needed

while on_race:
    tim.forward(speed + random.randint(-2, 2))
    tim.penup()
    tom.forward(speed  + random.randint(-2, 2))
    tom.penup()
    ben.forward(speed  + random.randint(-2, 2))
    ben.penup()
    arnold.forward(speed  + random.randint(-2, 2))
    arnold.penup()

    if tim.xcor() >= finish_line:
        print("Red is the winner")
        on_race = False
    elif tom.xcor() >= finish_line:
        print("Blue is the winner")
        on_race = False
    elif ben.xcor() >= finish_line:
        print("Green is the winner")
        on_race = False
    elif arnold.xcor() >= finish_line:
        print("Orange is the winner")
        on_race = False

screen.exitonclick()