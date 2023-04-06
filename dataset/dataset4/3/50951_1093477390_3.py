import Tkinter as tk
root=tk.Tk()

e=tk.Entry(width=10)
e.grid(row=0, sticky='e'+'w')

s=tk.Scrollbar(orient='horizontal')
s.grid(row=1, sticky='e'+'w')