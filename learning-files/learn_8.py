# Radio buttons and tkinter variables
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')


# doing it with a function, need to use global variable
def open():
    global myimage  # need to do this so it is not garbage collected
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap("./images/south_korea_15805.ico")

    path = Path("images/207ad028.bmp")
    myimage = ImageTk.PhotoImage(Image.open(
        path
    ))
    lbl = Label(top, text="Hello, world!",
                image=myimage, padx=100, pady=100).pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()


btn = Button(root, text="Open second window", command=open).pack()

# ----------------------
root.mainloop()
