from Tkinter import *

CLASSNAME = "Idle"

root = Tk( className=CLASSNAME )
root.wm_withdraw()

# A toplevel with a WM_CLASS
top1   = Toplevel( root, class_=CLASSNAME )
label1 = Label( top1, text="Toplevel 1" )
label1.pack()

# Another one
top2   = Toplevel( root, class_=CLASSNAME )
label2 = Label( top2, text="Toplevel 2" )
label2.pack()

root.mainloop()