# Entry widget
from tkinter import *

root = Tk()

# Add entry box
# -------------------
e = Entry(root, width=50, bg='#03396c', fg='#b3cde0', borderwidth=5)
e.pack()
e.insert(0, "Enter your name")  # Insert default value

# Add button
# -------------------


def myClick():
    myLabel = Label(root, text=f"Hello, {e.get()}")
    myLabel.pack()


myButton = Button(root, text="Enter your name", padx=6,
                  pady=2, fg='#b3cde0', bg='#03396c', command=myClick)
myButton.pack()

# ----------------------
root.mainloop()
