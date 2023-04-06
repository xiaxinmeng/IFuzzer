from tkinter import ttk
import tkinter as tk

root = tk.Tk()
tree = ttk.Treeview(root)
c = tree.insert('', 'end', text='This is critical message', tags='critical')
tree.insert(c, 'end', text='This is child of critical message', tags='critical')
for i in range(5):
    tree.insert('', 'end', text='This is non-critical message')
tree.tag_configure('critical', background='red', foreground="black")
tree.pack()
root.mainloop()