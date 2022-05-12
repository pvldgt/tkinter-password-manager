from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # create lists of letters, numbers and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # create lists of random letters, symbols and numbers
    letters_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for symbol in range(randint(2, 4))]
    number_list = [choice(numbers) for number in range(randint(2, 4))]

    # combine these random elements into one password list and randomly shuffle the elements
    password_list = letters_list + symbols_list + number_list
    shuffle(password_list)

    # turn the randomly generated list of elements into a password string
    ready_password = "".join([char for char in password_list])

    # first remove any pre-entered password, then insert the generated password into the password entry box
    password.delete(0, END)
    password.insert(0, ready_password)
    # copy the generated password into the clipboard
    pyperclip.copy(ready_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    """This function writes the website name, the username and
    the password into the 'all_passwords.json' file."""
    website_entry = website.get()
    username_entry = username.get()
    password_entry = password.get()
    new_dictionary = {
        website_entry: {
            "username": username_entry,
            "password": password_entry
        }
    }

    if website_entry != "" and password_entry != "":
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"Below ↓↓↓ are the details that you have entered for "
                                               f"{website_entry}\n"
                                               f"Username or email: {username_entry}\n"
                                               f"Password: {password_entry}")
        if is_ok:
            try:
                with open("all_passwords.json", "r") as file:
                    # read old data
                    data = json.load(file)
            # if the file doesn't exist yet, we'll create it and write the new dictionary to it
            except FileNotFoundError:
                with open("all_passwords.json", "w") as file:
                    json.dump(new_dictionary, file, indent=4)
            else:
                # update the old data with new data
                data.update(new_dictionary)
                # save the updated data to the json file
                with open("all_passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # once the password is added, the website and password entries get cleared
                website.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo(message="Password has been saved")
    else:
        messagebox.showinfo(message="Please don't leave any fields empty")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    """This function will check if there is an existing entry for this website
    and will retrieve the data associated with it, if found"""
    # grab the website entry
    website_entry = website.get()
    # read the json file
    try:
        with open("all_passwords.json", "r") as file:
            # read old data
            data = json.load(file)
    # if it doesn't exist, notify the user
    except FileNotFoundError:
        messagebox.showinfo(message="Nothing to search yet as there are no password saved")
    # check if the entry exists, if it does, display the details, if not, display an info message
    else:
        try:
            found_username = data[website_entry]["username"]
            found_password = data[website_entry]["password"]
        except KeyError:
            messagebox.showinfo(message="No details for this website exist")
        else:
            messagebox.showinfo(message=f"Here are the details for {website_entry}\n"
                                        f"Username: {found_username}\n"
                                        f"Password: {found_password}")
            # copy the password into the clipboard
            pyperclip.copy(found_password)


# ---------------------------- UI SETUP ------------------------------- #
# create the window
window = Tk()
# add the program title
window.title("Password Manager")
# set the padding
window.config(padx=40, pady=40)

# create the canvas for the logo
canvas = Canvas(width=200, height=200)
# load the image
lock_img = PhotoImage(file="logo.png")
# place the image on the canvas
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# email or username label
username_label = Label(text="Email/Username")
username_label.grid(column=0, row=2)

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# website entry
website = Entry(width=21)
website.grid(column=1, row=1)
# make the first entry box active (focused)
website.focus()

# email or username entry
username = Entry(width=35)
username.grid(column=1, row=2, columnspan=2)
# the entry box will have the most commonly used user email pre-entered
username.insert(0, "test@gmail.com")

# password entry
password = Entry(width=21)
password.grid(column=1, row=3)

# generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

# search button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
