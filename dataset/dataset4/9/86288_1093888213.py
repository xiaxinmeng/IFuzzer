import tkinter as tk
from tkinter import font
root = tk.Tk()
fnames = font.names(root)
f1 = font.Font(root=root, name=fnames[0], exists=True)
f2 = font.Font(root=root, name='TkFixedFont', exists=True)