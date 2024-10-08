from turtle import Screen, Turtle
import time
from snake_body import SnakeBody
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = SnakeBody()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Calling the move function
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect Collision with food

    if snake.segments[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Add collision with the snake body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
