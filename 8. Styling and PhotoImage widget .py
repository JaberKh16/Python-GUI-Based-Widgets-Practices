# importing the necessary modules
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image

# creating the window
root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()

button = ttk.Button(root, text='Click me!')
logo = ImageTk.PhotoImage(Image.open('F:\\Python Practice Work\\Files and Images\\download.gif'))

button.configure(image=logo, compound=CENTER)


root.mainloop()
