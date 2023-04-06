from tkinter import *
def _onMouseWheel(event):
    print(event)

root = Tk()
root.bind('<MouseWheel>',_onMouseWheel)