from turtle import Turtle, Screen
from paddle import Paddle
# Set up the screen 800 by 600 and divide it by 2
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
# Separete the two screen
divider = Turtle("square")
divider.color("white")
divider.penup()
divider.goto(0, 300)
divider.goto(0, -300)
divider.pendown()
divider.hideturtle()

paddle = Paddle()




screen.exitonclick()