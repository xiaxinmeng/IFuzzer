import tkinter as tk
from tkinter.font import Font
r = tk.Tk()
t = tk.Text(r, font=('Source Code Pro', 10, 'normal'))
t.pack()
s = '0oO !*}'
t.insert('1.0', s) # Only to check that all above is valid.
for c in s:
    print(Font(t, font=t['font']).measure(c))