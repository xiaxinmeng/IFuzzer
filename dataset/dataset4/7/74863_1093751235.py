
import tkinter as tk
from tkinter import ttk

def make_var_cb(root):
    v = tk.BooleanVar(root, True)
    cb = ttk.Checkbutton(root, text='Checkbutton', variable=v)
    cb.pack()
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    make_var_cb(root)
