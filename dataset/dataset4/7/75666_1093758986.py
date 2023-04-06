import tkinter as tk

root = tk.Tk()

def cmd1(event):
    print('1')

def cmd2(event):
    print('2')

def unbind1():
    l.unbind('<Motion>', b1)

def unbind2():
    l.unbind('<Motion>', b2)

l = tk.Label(root, text='Hover')

b1 = l.bind('<Motion>', cmd1)
b2 = l.bind('<Motion>', cmd2, True)

l.pack()
tk.Button(root, text='Unbind 1', command=unbind1).pack()
tk.Button(root, text='Unbind 2', command=unbind2).pack()

root.mainloop()