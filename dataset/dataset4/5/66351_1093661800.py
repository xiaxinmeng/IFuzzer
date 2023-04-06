import tkinter
widget = tkinter.Tk()
widget.tk.createfilehandler(file, tkinter.READABLE | tkinter.WRITABLE, callback)
...
widget.tk.deletefilehandler(file)