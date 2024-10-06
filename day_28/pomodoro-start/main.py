from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
timer = None
timer_running = False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_running, timer
    timer_running = False
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_message.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,timer_running
    if not timer_running:
        timer_running = True
        reps += 1

        WORK_MIN = 25
        SHORT_BREAK_MIN = 5 * 60
        LONG_BREAK_MIN = 20 * 60

        work_sec = WORK_MIN * 60

        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN)
            text_message.config(text="Break", fg=YELLOW)
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN)
            text_message.config(text="Short Break", fg=PINK)
        else:
            count_down(work_sec)
            text_message.config(text="Work", fg=RED)

#.................................Count Down.........................
def count_down(count):
    convert_min = math.floor(count / 60)
    convert_sec = (count % 60)
    if convert_sec < 10:
        convert_sec = f"0{convert_sec}"
    canvas.itemconfigure(timer_text, text=f"{convert_min}:{convert_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global timer_running
        timer_running = False  # Reset timer_running to prevent double-calling
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✓"  # Add check marks for each completed work session
        check_mark.config(text=mark)
        # Automatically start the next timer
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW) # space

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness = 0) # create canvas
tomato_file = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_file)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35 , "bold"))
canvas.grid(column=1, row=1)
# create label
text_message = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
text_message.grid(column=1, row=0)

# create check-mark label
check_mark = Label(text="")
check_mark.grid(column=1, row=3)


# create button
start_button = Button(text="Start", bg="white", command= start_timer)
start_button.grid(column=0, row=2)


# create second button
reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()