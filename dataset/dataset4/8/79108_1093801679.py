import tkinter as tk
import tkinter.filedialog as fd
 
root = tk.Tk()
 
def dostuff():
    fd.askopenfile()
 
bt = tk.Button(root, text="Click me!", command=dostuff)
bt.grid()
 
root.mainloop()