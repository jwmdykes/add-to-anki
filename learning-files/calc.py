# Calculator app
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg="#011f4b")

# Add entry box
# -------------------
e = Entry(root, width=35, bg='#03396c', fg='#b3cde0', borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "")  # Insert default value

# Add button
# -------------------
current_sum = 0


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def button_clear():
    global current_sum
    e.delete(0, END)
    current_sum = 0


def button_add():
    global current_sum
    num = e.get()
    num = int(num)
    current_sum += num
    e.delete(0, END)


def button_equal():
    button_add()
    global current_sum
    e.delete(0, END)
    e.insert(0, str(current_sum))


button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_click(1), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_click(2), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_click(3), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_click(4), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_click(5), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_click(6), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_click(7), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_click(8), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_click(9), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_click(0), bg="#03396c", fg="#b3cde0", borderwidth=2)
button_clear = Button(root, text="Clear", padx=80, pady=20,
                      command=button_clear, bg="#03396c", fg="#b3cde0", borderwidth=2)
button_equal = Button(root, text="=", padx=90, pady=20,
                      command=button_equal, bg="#03396c", fg="#b3cde0", borderwidth=2)
button_plus = Button(root, text="+", padx=40, pady=20,
                     command=button_add, bg="#03396c", fg="#b3cde0", borderwidth=2)
# putt buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

# -----------------------
root.mainloop()
