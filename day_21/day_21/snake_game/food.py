from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-285, 285)
        self.random_y = random.randint(-285, 285)
        self.goto(self.random_x, self.random_y)