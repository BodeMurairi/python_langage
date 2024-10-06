from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
# READ CSV_FILE
data = pd.read_csv("/home/bode/Documents/programming/100_days_ofCode/day_31/flash-card-project-start/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_card = current_card["French"]
    canvas_image.itemconfig(card_title, text= "French", fill= "black")
    canvas_image.itemconfig(card_word, text= french_card)
    canvas_image.itemconfig(card_background, image= card_front_image)
    
    flip_timer= window.after(3000, func=flip_card)

def is_known():
     global current_card, flip_timer
     window.after_cancel(flip_timer)
     current_card = random.choice(to_learn)
     french_card = current_card["French"]
     canvas_image.itemconfig(card_title, text= "French", fill= "black")
     canvas_image.itemconfig(card_word, text= french_card)
     canvas_image.itemconfig(card_background, image= card_front_image)
     if current_card in to_learn:
         to_learn.remove(current_card)
         data_saved = pd.DataFrame(to_learn)
         data_saved.to_csv("/home/bode/Documents/programming/100_days_ofCode/day_31/flash-card-project-start/data/words_to_learn.csv", index=False)
     flip_timer= window.after(3000, func=flip_card)


def flip_card():
    canvas_image.itemconfig(card_title, text= "English", fill = "white")
    canvas_image.itemconfig(card_word, text= current_card["English"])
    canvas_image.itemconfig(card_background, image= card_back_image)











#..................................................................GUI SETUP............................................................................................
window = Tk()
window.title("Flip Card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas_image = Canvas(width=800, height= 526)
card_front_image = PhotoImage(file="/home/bode/Documents/programming/100_days_ofCode/day_31/project/flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="/home/bode/Documents/programming/100_days_ofCode/day_31/project/flash-card-project-start/images/card_back.png")
card_background = canvas_image.create_image(400,263, image= card_front_image)
canvas_image.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas_image.create_text(400, 150, text="", font=("Calibri", 40))
card_word = canvas_image.create_text(400, 263, text= "", font=("Calibri", 60))
canvas_image.grid(column=0,row=0, columnspan=2)

# Buttons
yes_image = PhotoImage(file= "/home/bode/Documents/programming/100_days_ofCode/day_31/project/flash-card-project-start/images/right.png")
yes = Button(image=yes_image, highlightthickness=0, padx = 20, pady=20, width=100, height=100, command= is_known)
yes.grid(column=1, row=1)
no_image = PhotoImage(file= "/home/bode/Documents/programming/100_days_ofCode/day_31/project/flash-card-project-start/images/wrong.png")
no = Button(image=no_image, highlightthickness=0, padx = 20, pady=20, width=100, height=99, command=next_card)
no.grid(column=0, row=1)












next_card()

window.mainloop()
