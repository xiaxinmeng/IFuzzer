import Tkinter as tk
import ttk
root=tk.Tk()

e=ttk.Entry(width=10)
e.grid(row=0, sticky='e'+'w')

s=ttk.Scrollbar(orient='horizontal')
s.grid(row=1, sticky='e'+'w')