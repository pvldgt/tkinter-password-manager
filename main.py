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
canvas.grid(column=1, row=1)

window.mainloop()