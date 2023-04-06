import tkinter as tk
root = tk.Tk()
def test(*args):
    for arg in args:
        print(type(arg), '', repr(arg))
root.after(1, test, True, 1, '1')
root.mainloop()