import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import sql_util as sql
import add_to_anki as anki

colors = {
    'blue5': '#011f4b',
    'blue4': '#03396c',
    'blue3': '#005b96',
    'blue2': '#6497b1',
    'blue1': '#b3cde0',
}

font = ("Courier", 24)
small_font = ("Courier", 14)

root = tk.Tk()
root.title("Input a Korean English pair")
root.configure(bg=colors['blue5'])
width = 500
height = 300
root.geometry(f"{width}x{height}")
root.attributes('-alpha', 0.9)
root.attributes("-topmost", True)
root.overrideredirect(1)

# Use enter for buttons instead of space
root.bind_class("Button", "<Key-Return>", lambda event: event.widget.invoke())
root.unbind_class("Button", "<Key-space>")

# get command line arguments for position to open window at
# format: x position, y position then move the window there
# ---------------------------
if len(sys.argv) >= 3:
    xpos = sys.argv[1]
    ypos = sys.argv[2]
    xpos = int(xpos)
    ypos = int(ypos)
else:
    xpos = -1500
    ypos = 200
root.geometry(f"+{xpos-width//2}+{ypos-height//2}")

# use flex boxes
# -------------------------
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

frame = tk.Frame(root)
frame.configure(bg=colors['blue5'])

frame.grid(row=0, column=0, sticky="news", padx=3, pady=3)
# close window when focus goes outside the frame
frame.bind('<FocusOut>', lambda var: root.quit())
# root.bind('<FocusOut>', lambda var: root.quit())


class BlueBox():
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def show(self):
        tk.Grid.rowconfigure(frame, self.row, weight=1)
        tk.Grid.columnconfigure(frame, self.col, weight=1)
        self.widget = tk.Entry(
            frame,
            width=35,
            bg=colors['blue4'], fg=colors['blue1'],
            borderwidth=5,
            insertbackground=colors['blue1'],
            font=font)
        self.widget.grid(row=self.row, column=self.col, columnspan=3,
                         padx=10, pady=5, sticky="news")
        self.widget.insert(0, "")  # Insert default value
        self.widget.bind('<Key-Return>', lambda var: submit_form())


class BlueButton():
    def __init__(self, col, row, card, text, command=lambda: showinfo("default command", "default command")):
        self.col = col
        self.row = row
        self.card = card
        self.text = text
        self.command = command

    def show(self):
        tk.Grid.rowconfigure(frame, self.row, weight=1)
        tk.Grid.columnconfigure(frame, self.col, weight=1)
        self.widget = tk.Button(
            frame,
            text=self.text,
            padx=40, pady=5,
            command=self.command,
            bg=colors['blue4'], fg=colors['blue1'],
            borderwidth=2,
            font=font)
        self.widget.grid(row=self.row, column=self.col, columnspan=3,
                         padx=10, pady=10, sticky=self.card)


class BlueLabel():
    def __init__(self, col, row, card, text):
        self.col = col
        self.row = row
        self.card = card
        self.text = text

    def show(self):
        tk.Grid.rowconfigure(frame, self.row, weight=1)
        tk.Grid.columnconfigure(frame, self.col, weight=1)
        self.widget = tk.Label(
            frame,
            text=self.text,
            padx=40, pady=20,
            bg=colors['blue4'], fg=colors['blue1'],
            borderwidth=2,
            font=small_font
        )
        self.widget.grid(row=self.row, column=self.col, columnspan=3,
                         padx=10, pady=10, sticky=self.card)


korean_entry = BlueBox(col=0, row=0)
korean_entry.show()
korean_entry.widget.focus_set()

eng_entry = BlueBox(col=0, row=1)
eng_entry.show()


# submit logic


def submit_form():
    kor = korean_entry.widget.get()
    eng = eng_entry.widget.get()
    # showinfo("word submitted", f"korean: {ko}, english: {eng}")
    row = sql.Row(kor=kor, eng=eng)
    sql.add_row(row)
    anki.create()
    root.quit()


submit = BlueButton(col=0, row=2, card="se",
                    text="Submit", command=submit_form)
submit.show()

cancel = BlueButton(col=0, row=2, card="sw", text="Cancel", command=root.quit)
cancel.show()

# test = BlueLabel(0, 3, "news", f"Got command line vars: {xpos}, {ypos}")
# test.show()

# hotkeys
# -------------------------
root.bind('<Escape>', lambda var: root.quit())

root.mainloop()
