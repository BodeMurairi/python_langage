from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=600, height=300)
window.config(padx=100, pady=200)

# create a label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
my_label["text"] = "Bonjour"
my_label.config(text="Bienvenue!")

def welcome_page():
    my_label.config(text = "Welcome to my app")

button = Button(text= "Click me", command= welcome_page)
button.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=0, row=0)
input.get()










window.mainloop()