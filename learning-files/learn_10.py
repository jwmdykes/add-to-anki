# Sliders
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')
root.geometry("400x400")


def slide(var):
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


vertical = Scale(root, from_=300, to=600, command=slide)
vertical.grid(column=1, row=0, rowspan=3, sticky=NW)

horizontal = Scale(root, from_=300, to=600, orient=HORIZONTAL, command=slide)
horizontal.grid(column=0, row=1, columnspan=3, sticky=SW)


# ----------------------
root.mainloop()
