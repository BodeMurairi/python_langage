from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clean_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkeypress(move_backwards, "s")
screen.onkey(key='a', fun= move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun= clean_screen)
screen.exitonclick()