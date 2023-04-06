import tkinter as tk
from tkinter import ttk
root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()
tree.insert('', 1, iid='a b', text='id with space')
for item in tree.get_children():
    print(item)
    #tree.selection_add(item)  # fail
    #tree.selection_toggle(item)  # fail
    #tree.selection_set(item)  # fail
    #tree.selection_remove(item)  # fail
    tree.selection('add', item)  # fail