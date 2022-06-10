# importing the necessary module
from tkinter import *
from tkinter import ttk

# calling the tkinter class Tk()
root = Tk()

# creating the treeview instance
tree_view = ttk.Treeview()
# this doesnt do anything because till now nothing is being addded to the treeview widget
# but hover the mouse can see the treeview object
tree_view.pack()

# adding a item inside the tree view object
# Treeview.insert('parent', 'index', 'id_name', text= )
tree_view.insert('', '0', 'item1', text='Jara') # no parent '', index no 0, id-item1
tree_view.insert('', '1', 'item2', text='Gane' )

tree_view.insert('', '2', 'item3', text='Mostafa')
tree_view.insert('', '3', 'item4', text='Jaber') 
tree_view.insert('', '4', 'item5', text='Jubaer')

# configuring a new column 
tree_view.configure(column=('Age'))
# managing the width and position of the column
tree_view.column('Age', width=60, anchor='center')

# managing the column width and postion for the names
tree_view.column('#0', width=80, anchor='center')

# providing a heading for the column
# Treeview.heading('# column no', text=)
tree_view.heading('#0', text='Name')
tree_view.heading('#1', text='Age')

# setting a value for the 'Age' column
# Treeview.set('idname', 'column_name', 'value')
tree_view.set('item1', 'Age', '28')
tree_view.set('item2', 'Age', '38')
tree_view.set('item3', 'Age', '68')
tree_view.set('item4', 'Age', '24')
tree_view.set('item5', 'Age', '20')


# now provide a functionality to the Treeview object
def tree_view_selection(event):
    print(tree_view.selection()) # when select this fuinction will kicks

tree_view.bind('<<TreeviewSelect>>', tree_view_selection)


root.mainloop()