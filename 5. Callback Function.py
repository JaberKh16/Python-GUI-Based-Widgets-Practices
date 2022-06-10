# importing the necessary module
import tkinter as tk
from tkinter import ttk 

# creating the tkinter window
root = tk.Tk()

# adding the button
button_1 = ttk.Button(root, text="Click me!")
button_1.pack()

button_2 = ttk.Button(root, text="Click me!")
button_2.pack()

def button_click_1(ID):
    print("ID is :{}".format(ID))

# here's the button doesnt working right , why because we didnt enable it
button_1.configure(command= button_click_1(ID =10))

def button_click_2(ID):
    print("ID is :{}".format(ID))

# here's the button does working on button click 
button_2.configure(command= lambda : button_click_2(ID =10))

root.mainloop()