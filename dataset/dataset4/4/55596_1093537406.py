import sys
if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
else:
    import Tkinter as tk
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog

class App():  
    def __init__(self):
        self.root = tk.Tk()
        
        self.btnMsg = tk.Button(self.root, text='Click me')
        self.btnMsg.pack()
        self.btnMsg.bind('<Button-1>', self.clickMsg)
        
        self.btnFd = tk.Button(self.root, text='Click me too')
        self.btnFd.pack()
        self.btnFd.bind('<Button-1>', self.clickFd)
        
        self.btnCommand = tk.Button(self.root, text='And now click me')
        self.btnCommand.pack()
        self.btnCommand.config(command=self.clickCommand)

        self.root.mainloop()
        
    def clickMsg(self, event):
        messagebox.showerror(title='Error!', message='The button is sunken!')
   
    def clickFd(self, event):
        filedialog.askdirectory(title='Choose a directory')
        
    def clickCommand(self):
        messagebox.showinfo(title='Success!', message='The button is raised.')
        
App()