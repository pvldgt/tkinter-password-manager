from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    """This function writes the website name, the username and
    the password into the 'all_passwords.txt' file."""
    website_entry = website.get()
    username_entry = username.get()
    password_entry = password.get()
    full_line = f"{website_entry} | {username_entry} | {password_entry}\n"

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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()