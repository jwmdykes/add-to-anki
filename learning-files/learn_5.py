# Entry widget
from tkinter import *
from PIL import ImageTk, Image
import os
from pathlib import Path

root = Tk()
root.title('Adding icons')
root.iconbitmap('./images/south_korea_15805.ico')

# Put images in list
images = []
image_dir = Path("images")
for path in image_dir.iterdir():
    try:
        images.append(ImageTk.PhotoImage(Image.open(
            path
        ).resize((500, 500))))
    except Exception as e:
        print(e)

# show first image
# ----------------------
image_index = 0
my_label = Label(image=images[image_index])
my_label.grid(row=0, column=0, columnspan=3)

# show status with current image index
status = Label(
    root, text=f"Image {image_index+1} of {len(images)}", bd=1, relief=SUNKEN)
status.grid(row=2, column=0, columnspan=3, sticky=E)


# Button to loop between images
def next_image():
    global image_index
    global my_label
    image_index = (image_index + 1) % (len(images) - 1)

    my_label.grid_forget()
    my_label = Label(image=images[image_index])
    my_label.grid(row=0, column=0, columnspan=3)


def last_image():
    global image_index
    global my_label
    image_index = (image_index - 1) & (len(images)-1)

    my_label.grid_forget()
    my_label = Label(image=images[image_index])
    my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=last_image, padx=20)
button_exit = Button(root, text="Exit", command=root.quit, padx=20)
button_forward = Button(root, text=">>", command=next_image, padx=20)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

# ----------------------
root.mainloop()
