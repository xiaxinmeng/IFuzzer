import tkinter

root = tkinter.Tk()
root.minsize(300, 300)
root.maxsize(500, 500)
root.resizable(False, False)

def bigger(e):
    size = root.winfo_width() + 20
    root.resizable(True, True)
    root.geometry(f'{size}x{size}')
    root.resizable(False, False)

def smaller(e):
    size = root.winfo_width() - 20
    root.resizable(True, True)
    root.geometry(f'{size}x{size}')
    root.resizable(False, False)

root.bind('<Button-4>', bigger)
root.bind('<Button-5>', smaller)
root.mainloop()