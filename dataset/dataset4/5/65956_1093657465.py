from Tkinter import *

root=Tk()

def hello():
    print('hello!')

def toggle():
	print('I think the menu bar is %s' % menubar.entrycget(0, 'state'))
	if menubar.entrycget(0, 'state')=='normal':
		print('disabling')
		menubar.entryconfig(0,state=DISABLED)
		print('disbled')
	else:
		print('enabling')
		menubar.entryconfig(0,state=NORMAL)
		print('enabled')

menubar = Menu(root)
submenu = Menu(menubar, tearoff=0)
submenu.add_command(label='Hello', command=hello)
menubar.add_cascade(label='test', menu=submenu)

# this cascade will have index 0 in submenu
b = Button(root, text='Toggle', command=toggle)
b.pack()

# display the menu
root.config(menu=menubar)
root.mainloop()