# importing the necessary module
import tkinter as tk
from tkinter import ttk
from tkinter.constants import END 

# creating the tkinter window
root = tk.Tk()

entry_1 = ttk.Entry(root, width=40)
entry_1.grid(row=0, column=0, columnspan=3)

# deleting entries full
button_1 = ttk.Button(root, text="Full Entry Delete!")
button_1.grid(row=1, column=0)

# deleting entries partial
button_2 = ttk.Button(root, text="Partial Entry Delete!")
button_2.grid(row=1, column=1)

# insering entries full
button_11 = ttk.Button(root, text="Full Entry Insert!")
button_11.grid(row=2, column=0)

# insering entries partial
button_22 = ttk.Button(root, text="Partial Entry Insert!")
button_22.grid(row=2, column=1)

# full entry deletion function
def button_click_1():
    print(entry_1.get())
    # Deleting the enrty
    # this will delete the whole entry
    print(entry_1.delete(0, END)) # return none as no enrty is available

# partial entry deletion function    
def button_click_2():
    print(entry_1.get())
    # Deleting the enrty
    # this will delete the entry 0 to 4th word
    print(entry_1.delete(0, 4)) # return none as no enrty is available

button_1.configure(command=button_click_1)
button_2.configure(command=button_click_2)

# Full entry insertion function    
def button_click_11():
    #print(entry_1.get())
    # inserting the enrty
    # this will insert the entry 0 to END word
    print(entry_1.insert(0, entry_1.get())) # return 0 to END though enrty is available

# partial entry insertion function    
def button_click_22():
    #print(entry_1.get())
    # inserting the enrty
    # this will insert the entry 0 to 4th word
    print(entry_1.insert(0, entry_1.get()[0:4])) # return 0 to 4th though enrty is available

button_11.configure(command=button_click_11)
button_22.configure(command=button_click_22)

root.mainloop()