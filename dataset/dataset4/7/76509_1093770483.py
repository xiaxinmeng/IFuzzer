from Tkinter import *
from ttk import *

root = Tk()
tv = Treeview(root, columns=("foobar",))

tv.heading("foobar", text="Foobar!")
tv.column("#0", width=0)
tv.column("foobar", stretch=True, minwidth=100, width=400)
tv.grid()

kw = {'values': '" ";', 'tags': ''}
tv.insert("", END, iid=None, **kw)

root.mainloop()