from Tkinter import Tk
from tkSimpleDialog import askstring

def close_handler():
    askstring('', '')
    root.destroy()

root = Tk()
root.protocol('WM_DELETE_WINDOW', close_handler)
root.mainloop()