import tkinter
import tkinter.font

f = tkinter.font.Font(family='Arial', size=30)
root = Tk()
label = tkinter.Label(root, text="Hello", font=f)
label.pack()