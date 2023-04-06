import tkinter
#import tkinter.font
root = tkinter.Tk()
ft = tkinter.font.Font(family = 'Fixdsys',size = 20,weight = tkinter.font.BOLD)
tkinter.Label(root,text = 'hello sticky',font = ft ).grid()
root.mainloop()