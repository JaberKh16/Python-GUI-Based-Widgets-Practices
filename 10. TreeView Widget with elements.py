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

# moving items to single root
# Treeview.move('parent_name', child_name, index value)
tree_view.move('item4', 'item3', '2')
tree_view.move('item5', 'item3', '2')

# add another new item and make item3 as the parent
tree_view.insert('item3', '0', 'item6', text='Mahmud' )

# by default making a parent directory open via code
# Treeview.item(which item(id) to open, set open = True)
tree_view.item('item3', open=True)

# hide any item via code
# Treeview.detach(idname)
# cant see the id = 4 item,, thinks its get deleted , no it basically hide itself
tree_view.detach('item4') 

# how? check it now via moving the id item
tree_view.move('item4', '', 'end')

# deleting the first item
tree_view.delete('item1') # defines the item(id) which you want to delete

root.mainloop()