import Tkinter as tk
import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree.insert("","end",values=("one","two","bam! {"))

root.mainloop()