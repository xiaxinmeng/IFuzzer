import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
w = ttk.LabeledScale(root)
w.pack()
w.scale.set(1)
root.mainloop()