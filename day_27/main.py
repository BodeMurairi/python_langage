from tkinter import *

window = Tk()
window.title("Miles to km converter simple GUI App")
window.config(padx=30, pady=30)

# Text entry
input_entry = Entry(width=10)
input_entry.grid(column=0, row=0)

# Raise exception
def get_float_value():
    try:
        user_input = float(input_entry.get())
        return user_input
    except ValueError:
        print("Please enter a valid number.")

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)
to_label = Label(text="To")
to_label.grid(column=0, row=2)
km_entry = Entry(width=10)
km_entry.grid(column=0, row=3)
km_entry.get()
km_label = Label(text="Kilometers")
km_label.grid(column=1, row=3)

def convert():
    user_input = get_float_value()
    if user_input is not None:
        kilometers = user_input * 1.609344
        km_entry.delete(0, END)  # Clear the previous value
        km_entry.insert(0, str(kilometers))

# Button
get_value_button = Button(window, text="Get Value", command=get_float_value)
get_value_button.grid(column=0, row=2)

convert_button = Button(text="Calculate", command=convert)
convert_button.grid(column=0, row=4)

window.mainloop()