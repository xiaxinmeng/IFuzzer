import tkinter as tk

class Hello(tk.Frame):                     
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        check = tk.Checkbutton(self, text='Checkbutton')
        check.pack()

root = tk.Tk()
Hello(root).pack()
Hello(root).pack()
root.mainloop()