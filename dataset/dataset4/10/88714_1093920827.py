
from tkinter import *
from tkinter.ttk import *
import time

window = Tk()
window.title('Test')
window.geometry('400x250+1000+300')


pb = Progressbar(window, orient=HORIZONTAL, length=100, mode='indeterminate')
pb.pack(expand=True)

Button(window, text='Start', command=pb.start).pack()

window.mainloop()
