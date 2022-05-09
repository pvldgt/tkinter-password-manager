from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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
    the password into the 'all_passwords.txt' file."""
    website_entry = website.get()
    username_entry = username.get()
    password_entry = password.get()
    full_line = f"{website_entry} | {username_entry} | {password_entry}\n"

    if website_entry != "" and password_entry != "":
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"Below ↓↓↓ are the details that you have entered for "
                                               f"{website_entry}\n"
                                               f"Username or email: {username_entry}\n"
                                               f"Password: {password_entry}")
        if is_ok:
            with open("all_passwords.txt", "a") as file:
                file.write(full_line)
                # once the password is added, the website and password entries get cleared
                website.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo(message="Password has been saved")
    else:
        messagebox.showinfo(message="Please don't leave any fields empty")


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
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
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

window.mainloop()
