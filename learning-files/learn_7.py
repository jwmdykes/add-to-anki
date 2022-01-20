# Radio buttons and tkinter variables
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    messagebox.showinfo("This is my Popup!", "Hello World!")


def popup_yesno():
    response = messagebox.askyesno("Yes or no popup", "Yes or no?")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text="Showinfo", command=popup).pack()
Button(root, text="Askyesno", command=popup_yesno).pack()

# ----------------------
root.mainloop()
