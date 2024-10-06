from turtle import Turtle, Screen

# Create a class that inhesrits from the Turtle class

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4,2)
        self.penup()
        self.goto(350, 0)

    # def key press movement up and down
    def go_up(self):
        self.setheading(90)
        self.forward(20)

    def go_down(self):
        self.setheading(270)
        self.forward(20)

    def up(self):
        self.onkeypress(self.go_up, "Up")
        self.listen()
    def down(self):
        self.onkeypress(self.go_down, "Down")
        self.listen()