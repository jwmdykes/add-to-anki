# adding Buttons
from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", padx=6,
                  pady=2, fg='#b3cde0', bg='#03396c', command=myClick)
myButton.pack()

root.mainloop()
