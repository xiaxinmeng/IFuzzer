
from tkinter import *
def keyup(e):
    print('up', e.__dict__)
def keydown(e):
    print('down', e.__dict__)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()
