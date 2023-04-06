import Tkinter

root = Tkinter.Tk()
waitVar = Tkinter.BooleanVar()

root.after(3000, lambda: waitVar.set(True))
root.wait_variable(waitVar)