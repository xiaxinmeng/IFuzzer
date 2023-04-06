def truebug():

    import Tkinter
    Tk = Tkinter
    top = Tk.Toplevel()
    f = Tk.Frame(top)
    f.pack()
    var = Tk.IntVar()
    box = Tk.Checkbutton(f, anchor="w", 
text="box",variable=var)
    box.pack()
    var.set(True)
    val = var.get()