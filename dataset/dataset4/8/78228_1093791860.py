import tkinter

root = tkinter.Tk()

text = tkinter.Text(root)
vbar = tkinter.Scrollbar(root)

vbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

text.config(yscrollcommand=vbar.set)
vbar.config(command=text.yview)

lines = ['This is the line number %d.\n' % i for i in range(200)]
text.insert(tkinter.END, ''.join(lines))