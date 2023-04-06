import tkinter
root = tkinter.Tk()
widget = tkinter.Menubutton(root)
for value in (True, 1, 'true', 'yes', 'on'):
    print(value, flush=True)
    widget['indicatoron'] = value