from oxogame import *

class MainWindow(Frame):
    def __init__(self, master=None):
        " Initialise main window with controls "
        Frame.__init__(self, master)
        master.title('Font problem')
        ttk.Style().configure('Square.TButton', font='Arial 24 bold', width=1, height=1, padding=(6,0))