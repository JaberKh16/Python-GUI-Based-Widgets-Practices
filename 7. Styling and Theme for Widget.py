# importing the necessary module
import tkinter as tk
from tkinter import ttk
from tkinter.constants import ACTIVE

# creating the tkinter window
root = tk.Tk()

button_1 = ttk.Button(root, text='Button 1')
button_1.pack()

button_2 = ttk.Button(root, text='Button 2')
button_2.pack()

button_3 = ttk.Button(root, text='Button 3')
button_3.pack()


# styling the widget
# creating the Style instance
style = ttk.Style()
# getting the style information available on this OS
print(style.theme_names()) # returns the style available in this OS 

# checking the style used in OS
print(style.theme_use()) # returns the style used in this OS

# changing the style format from the available OS theme style
style.theme_use('winnative') # returns the style provide the theme_use()

# applying foreground color for all the button
# checking button class first
print(button_1.winfo_class()) # returns the button class name

# now changing the foreground for all the button using the button class
style.configure('TButton', foreground = 'Blue') # returns all trhe button widget foreground color is blue

# changing the font also with arial and size 24 ,, font=('font_name', font_size, 'font_type')
style.configure('TButton', foreground ='Blue', font=('Roman', 34))

# changin the specification for specific button
style.configure('Info.TButton', foreground='Red', font=('Arial', 20))
# i want to change the button 2 information
button_2.configure(style='Info.TButton')

# maping the button 3 with some background color
style.map('Info.TButton', background=[('pressed','green'), ('disabled','gray')])
button_3.configure(style='Info.TButton')
button_3.state(['disabled'])
root.mainloop()