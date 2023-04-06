import os
del os.environ['DISPLAY']
import Tkinter
Tkinter.Tk()
Tkinter.Tcl().loadtk() # should hang now (with a proper tk version)