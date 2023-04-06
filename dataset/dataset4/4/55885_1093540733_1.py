import sys,imp
imp.load_module('tkinter',*imp.find_module('tkinter'))
imp.load_module('tkinter.ttk',*imp.find_module('ttk',
  sys.modules["tkinter"].__path__))
"ttk" in dir(sys.modules['tkinter']) # False
from tkinter import ttk # ImportError