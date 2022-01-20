import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="안녕하세요 은혜",
    fg="white",
    bg="black",
    width=20,
    height=10
)
label.pack()

# Adjust size
window.geometry("500x300")

# Create transparent window
window.attributes('-alpha', 0.8)
# window.wm_attributes('-type', 'splash')

# lift to top and focus
window.lift()
window.attributes('-topmost', True)
window.after_idle(window.attributes, '-topmost', False)
window.after(1, lambda: window.focus_force())
window.mainloop()
