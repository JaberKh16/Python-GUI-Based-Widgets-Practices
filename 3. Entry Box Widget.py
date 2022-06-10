# importing the necessary module
import tkinter as tk
from tkinter import ttk 

# creating window
root = tk.Tk()

entry_1 = ttk.Entry(root, width=40)
entry_1.pack()

button_1 = ttk.Button(root, text="Click me!")
button_1.pack()

def button_click():
    print(entry_1.get())

# configure the button 
button_1.configure(command=button_click)

root.mainloop()