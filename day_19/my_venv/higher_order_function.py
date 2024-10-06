from turtle import Turtle, Screen

b = Turtle()

s = Screen()

def move_forwards():
    b.forward(10)


s.listen()
s.onkey(key="space", fun= move_forwards)
s.exitonclick()