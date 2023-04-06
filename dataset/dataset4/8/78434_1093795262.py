
import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
# root.update() # remove comment to fix the problem
showinfo('alert', 'this parrot is dead!')
root.mainloop()
