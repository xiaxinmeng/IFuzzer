import tkinter
import tkinter.font

root = tkinter.Tk()
w = tkinter.Frame(root)
f = tkinter.font.Font(root, family='Arial', size=30)
label = tkinter.Label(w, text="Hello", font=f)
label.pack()
w.pack()
root.mainloop()