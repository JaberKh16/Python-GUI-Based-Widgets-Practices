# importing the necessary module
from tkinter import *
from tkinter import ttk

# calling tkinter class Tk()
root = Tk()

# creating the treeview instance
tree_view = ttk.Treeview()
# this doesnt do anything because till now nothing is being addded to the treeview widget
# but hover the mouse can see the treeview object
tree_view.pack()



root.mainloop()