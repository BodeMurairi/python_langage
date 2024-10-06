from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeBody:
    """Controls the snake body."""

    def __init__(self):
        """Creates different snake segments."""
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_segments()

    def create_segments(self):
        """Creates the snake segments."""
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_segments()

    def extend(self):
        # Add a new segment to the snake body
        self.add_segment(self.segments[-1].position())


    def move(self):
        """Moves the snake forward."""

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        # Adjust the snake size as needed
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading != 270:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading != 90 :
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading != 0:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading != 180:
            self.segments[0].setheading(RIGHT)
