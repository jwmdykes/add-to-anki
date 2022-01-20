# Grid system
from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is ulazy!")
myLabel3 = Label(root, text="               ")

# can also do
# myLabel2 = Label(root, text="My name is ulazy!").grid(row=0, column=0)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=3)
myLabel3.grid(row=0, column=2)


root.mainloop()
