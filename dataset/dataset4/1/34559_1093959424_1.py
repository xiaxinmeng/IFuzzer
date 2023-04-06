from Tkinter import *

def testwindow(mess):
    root = Tk()

    w = Label(root, text="[ %s ]" % mess)
    w.pack()

    root.mainloop()

testwindow("Hello World")