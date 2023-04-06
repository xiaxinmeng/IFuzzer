from tkinter import *
root = Tk()
text = Text(root)
text.pack()
text.focus_set()  # required to work
root.mainloop()