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


# checking the button state using instate(statespec)
# statespec argument to tell that if its disabled or not
print(button_1.instate(statespec=['!disabled']))

# now disabling the the button using state(statespec=['disabled])
# this will disabled the button status
button_1.state(statespec=['disabled'])

root.mainloop()