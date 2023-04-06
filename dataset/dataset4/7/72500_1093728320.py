from tkinter import *
from tkinter.ttk import *

root = Tk()

root.option_add("*Font", "sans-serif 12")

s = Style()
s.configure('TButton', font=('courier', 40))
s.configure('TLabel', font=('courier', 40))