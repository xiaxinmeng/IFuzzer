from tkinter import Tk
from tkinter.messagebox import askokcancel, showerror


master=Tk()
showerror('Error', 'Error message', parent=master)
a = askokcancel('Error', 'Error message', parent=master)
master.mainloop()