import tkinter as tk
from tkinter import ttk
from idlelib.run import fix_scaling

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()
fix_scaling(root)

tree.insert('', 'end', 'widgets', text='Widget Tour')
tree.insert('', 0, 'gallery', text='Applications')
id = tree.insert('', 'end', text='Tutorial')
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')

root.mainloop()