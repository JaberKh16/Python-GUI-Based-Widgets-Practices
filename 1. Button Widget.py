# importing the necessary module
import tkinter as tk
from tkinter import ttk

# creating the tcl window
root = tk.Tk(screenName=None, baseName=None, className='Tix')

# creating button widget
button_1 = ttk.Button(root, text="Click me!")
button_1.pack()

# button functionality work
def Button_Work():
    print("Button has been clicked.")

# to configure the button widgets vairable
button_1.config(command= Button_Work)

# invoking the function without calling just use the invoke() which will automatically 
# invoke the function.
button_1.invoke() # note: invoke() invokes the function and return None as the return value

root.mainloop()