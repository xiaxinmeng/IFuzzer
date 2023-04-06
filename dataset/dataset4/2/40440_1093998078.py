import Tkinter

root = Tkinter.Tk()
waitvar = Tkinter.BooleanVar()

root.after(50, lambda: waitvar.set(True))
root.after(10, root.destroy)
root.wait_variable(waitvar)

root.mainloop()