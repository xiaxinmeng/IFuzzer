import tkinter as tk
from tkinter import ttk

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

w = tk.Tk()
ttk.Checkbutton(w, text = "Checkbox").grid()
w.mainloop()