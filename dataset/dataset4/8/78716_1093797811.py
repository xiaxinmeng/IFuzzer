import tkinter as tk

root = tk.Tk()
cbid = None
cbcount = 0

def cb():
    global cbid, cbcount
    cbcount += 1
    cbid = root.after(1, cb)

def cbcancel():
    print(cbcount)
    root.after_cancel(cbid)

root.after(1000, cbcancel)
cbid = root.after(1, cb)
root.mainloop()