#### bug.py
import tkinter

def mouse_wheel(event):
    print('Mouse wheel event')

tk = tkinter.Tk()
list = tkinter.Listbox(tk)
list.bind('<MouseWheel>', mouse_wheel)
for n in range(20):
    list.insert(tkinter.END, str(n**n))
list.pack(fill=tkinter.BOTH, expand=1)
tk.mainloop()
####