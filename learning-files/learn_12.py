# Drop down boxes
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')
root.geometry("400x400")


def show():
    myLabel = Label(text=clicked.get()).pack()


clicked = StringVar()
clicked.set("Monday")

options = ["Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday"]

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='Show Selection', command=show).pack()

# ----------------------
root.mainloop()
