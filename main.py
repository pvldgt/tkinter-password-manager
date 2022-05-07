from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# create the window
window = Tk()
# add the program title
window.title("Password Manager")
# set the padding
window.config(padx=20, pady=20)

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
website_entry = StringVar()
website = Entry(textvariable=website_entry, width=35)
website.grid(column=1, row=1, columnspan=2)

# email or username entry
username_entry = StringVar()
username = Entry(textvariable=username_entry, width=35)
username.grid(column=1, row=2, columnspan=2)

# password entry
password_entry = StringVar()
password = Entry(textvariable=username_entry, width=21)
password.grid(column=1, row=3)

# generate password button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()