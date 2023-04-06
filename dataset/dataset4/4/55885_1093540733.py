import sys, tkinter
"ttk" in dir(sys.modules['tkinter']) # False
import tkinter.ttk
"ttk" in dir(sys.modules['tkinter']) # True