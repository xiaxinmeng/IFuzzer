import tkinter
t = tkinter.Text()
t.pack()
t.bind("<<Selection>>", print)
t.bind("<<debug>>", print)
for k in tkinter.EventType:
    try:
        t.event_add("<<debug>>", '<%s>' % k)
    except tkinter.TclError:
        pass

tkinter.mainloop()