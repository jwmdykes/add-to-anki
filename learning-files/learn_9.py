# Radio buttons and tkinter variables
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')

root.filename = filedialog.askopenfilename(initialdir=".", title="Select A File", filetype=(
    ("png files", "*.png"), ("all files", "*.*")))
path = Path(root.filename)
my_label = Label(root, text=str(path)).pack()

# ----------------------
root.mainloop()
