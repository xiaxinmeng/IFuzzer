import tkinter

root = tkinter.Tk()

text = tkinter.Text(root)
vbar = tkinter.Scrollbar(root)

vbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

text.config(yscrollcommand=vbar.set)
vbar.config(command=text.yview)

lines = ['This is the line number %d.\n' % i for i in range(256)]
text.insert(tkinter.END, ''.join(lines))
 
def click_trace(event):
    text.insert('%d.%d' % (1, 0), 'Clicked at (%d,%d) on %s.\n' % (event.x, event.y, vbar.identify(event.x, event.y)))

vbar.bind('<Button-1>', click_trace)

root.mainloop()