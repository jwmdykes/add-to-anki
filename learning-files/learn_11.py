# Checkboxes
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = IntVar()

c = Checkbutton(root, text="Check this box!", variable=var)
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

# ----------------------
root.mainloop()
