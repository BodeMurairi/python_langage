import json
from tkinter import *
from tkinter import messagebox
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    length = random.randint(8, 32)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email":email,
        "password":password
    }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) ==0:
        messagebox.showerror(title="Error!", message="Please fill in all fields.")
        return
    else:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
        with open("passwords.json", "w") as data_file:
            # save it to json file
            json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# Logo
canvas_image = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="/home/bode/Documents/programming/100_days_ofCode/day_29/my_venv/password-manager-start/logo.png")
canvas_image.create_image(100, 100, image=image)
canvas_image.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg="black")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", fg="black")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", fg="black")
password_label.grid(column=0, row=3)

# Entry fields
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22, show="*")  # Hide password characters
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(
    text="Generate Password", width=21, command=generate_password
)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add Password", width=36, command=save)
add_button.grid(column=1, row=4)

root.mainloop()