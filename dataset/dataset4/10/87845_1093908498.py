import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll, pointer, wintypes
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
btn1 = tk.Button(root, text='btn1').pack(side=tk.LEFT)
sg = ttk.Sizegrip(root).pack(side=tk.LEFT)
btn2 = tk.Button(root, text='btn2').pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
root.mainloop()