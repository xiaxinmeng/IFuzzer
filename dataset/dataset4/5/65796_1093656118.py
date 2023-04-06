from tkinter import *
from tkinter import ttk

paned = ttk.Panedwindow(orient="horizontal")
left = ttk.Frame(paned)
left.pack(side='left', fill='both', expand=True)
right = ttk.Frame(paned)
right.pack(side='right', fill='both', expand=True)
button = ttk.Button(left,text="lefgt pane")
button.pack( fill='both', expand=True)
button2 = ttk.Button(right, text="right pane")
button2.pack( fill='both', expand=True)
paned.add(left)
paned.add(right)
paned.pack(fill="both",expand=True, pady = (4,1), padx=4)

mainloop()