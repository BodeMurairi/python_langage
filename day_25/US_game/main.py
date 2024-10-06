import turtle as t
from turtle import Turtle
import pandas as pd

# Set up the screen
screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
alignment = "center"
font = ("Courier", 24, "bold")
# Add image on the screen
screen.addshape(image)
t.shape(image)

# Load CSV file
states = pd.read_csv("50_states.csv")
states_names = states["state"]  # State name
states_names = states_names.to_list()  # Save states data into a list
# Question pop-up

# Create a list to store written states
score = 0  # Add a score tracker
previous_score = 0  # Initialize previous score
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States correct" , prompt="What is another state's name?").title()

    missing_states = []
    if answer_state == "Exit":
        missing_states = [state for state in states_names if state not in guessed_states]
        missing_states = pd.Series(missing_states)
        states_to_learn = missing_states.to_csv("StatesToLearn.csv")
        break

    if answer_state in states["state"].values:
        # Check if the state has already been written
        guessed_states.append(answer_state)
        row_choice = states[states["state"] == answer_state]
        x_coordinate = row_choice["x"].values[0]
        y_coordinate = row_choice["y"].values[0]
        b = Turtle()  # Create another turtle to handle response
        b.hideturtle()
        b.penup()
        b.goto(x_coordinate, y_coordinate)
        b.write(answer_state)
        c = Turtle()
        c.hideturtle()
        c.penup()
        score += 1

t.mainloop()
