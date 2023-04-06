import tkinter
def callback():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()