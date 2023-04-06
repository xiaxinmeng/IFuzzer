from Tkinter import *

def dialog():
    win = Toplevel()
    Label(win, text='Modal Dialog').pack()
    win.transient(win.master)
    win.focus_set()
    win.grab_set()
    win.wait_window()

root = Tk()
Button(root, text='Custom Dialog', command=dialog).pack()
root.mainloop()