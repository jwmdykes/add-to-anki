# Radio buttons and tkinter variables
from tkinter import *
from PIL import ImageTk, Image
import os
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')

# r = IntVar()
# r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# radio button
# Radiobutton(root, text="Option 1", variable=r, value=1,
#             command=lambda: clicked(r.get())).pack(padx=100, pady=10)
# Radiobutton(root, text="Option 1", variable=r, value=2,
#             command=lambda: clicked(r.get())).pack(padx=100, pady=10)

# myLabel = Label(root, text=pizza.get())
# myLabel.pack(padx=100, pady=10)

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

# ----------------------
root.mainloop()
