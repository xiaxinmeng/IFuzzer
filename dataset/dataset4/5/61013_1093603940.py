#test.py
import tkinter as tk

root = tk.Tk()
b = tk.Button(root, text='Button')
b.grid()
print(b.grid_info())
root.mainloop()