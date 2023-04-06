
from tkinter import Tk, Text
r = Tk()
t = Text(r)
t.pack()
t.insert('insert', 'Hello gregarious Jim')
#t.tag_config('red', background='white', foreground='red')
# Selection does not change 'gregarious'.
t.tag_config('red', foreground='red')
# Selection changes background only.
# In first, cannot see boundaries of selection unless both outside.
t.tag_add('red', '1.6', '1.16')
# Default selection on Windows 10 is white on blue.
t.tag_config('sel', background='lightgray', foreground='blue')
# Adding this does not affect notes above.
# TBD. What if change default for widget?
