import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="black",
                fieldbackground="black", foreground="white")
tree = ttk.Treeview(root)
tree.insert("", 0, "item", text="item")
tree.pack()
root.mainloop()