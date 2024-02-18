import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor(title = "Select Color")
    if color[1] is not None:
        print("Selected color: ", color[1])
        # Do something with the selected color

root = tk.Tk()
button = tk.Button(root,text = "Pick Color", command = pick_color())
button.pack()

root.mainloop()