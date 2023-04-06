import numpy as np
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(width=400,
                   height=400,
                   background="bisque")
canvas.pack(fill="both", expand=True)
line = canvas.create_line([[100, 100], [300, 300]])
canvas.coords(line, [[100, 100], [200, 200]])  # line with error
