
import tkinter as tk
from functools import partial

def _mapped(method, widget, *args, **kwargs):
    getattr(widget, method)(*args, **kwargs)
    return widget

packed = partial(_mapped, 'pack')
gridded = partial(_mapped, 'grid')
placed = partial(_mapped, 'place')

root = tk.Tk()

label1 = gridded(tk.Label(root), row=0, column=0)
label2 = gridded(tk.Label(root), row=0, column=1)
label3 = gridded(tk.Label(root), row=0, column=2)
