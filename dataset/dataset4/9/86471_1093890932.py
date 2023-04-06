import tkinter as tk

from tkinter import auto_complete

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

entry = auto_complete.AutocompleteEntry(frame)
# You can pass additional parameters to further customize the window;
# all parameters that you can pass to tk.Frame, are valid here too.