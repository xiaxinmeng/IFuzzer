import tkinter as tk
from tkinter.font import Font
root=tk.Tk()
f = Font(name='TkFixedFont', exists=True, root=root)
print(Font.actual(f))