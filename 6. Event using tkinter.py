# importing the necessary module
import tkinter as tk
from tkinter import ttk

# creating the tkinter window
root = tk.Tk()

button_1 = ttk.Button(root, text="Click me!")
button_1.pack()

def button_press(event):
    print("Button is pressed")
    
def key_press(event):
    print("type:{}".format(event))

# bind(event_key_name, function)
root.bind("<Control-c>", key_press)
button_1.bind("<ButtonPress>", button_press)

root.mainloop()