import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns="1 2 3")
tree.tk.call(tree, "insert", "", "end" , "-values", ("one","two","bam! {"))
tree.grid()

root.mainloop()