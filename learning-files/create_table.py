# Creating a basis database with sqlite3
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import sqlite3

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')
root.geometry("400x400")

# Create connection to database
conn = sqlite3.connect("./data/address_book.db")
# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")


# Commit changes
conn.commit()
# Close connection
conn.close()

# ----------------------
root.mainloop()
