import tkinter as tk
from tkinter import ttk
r = tk.Tk()
l = ttk.Label(r, text='colored label', background='red')
l.pack()
r.mainloop()  # if not in IDLE