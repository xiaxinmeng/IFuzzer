import tkinter as tk
master = tk.Tk()
e = tk.Entry(master)
e.pack()
e.focus_set()
def callback():
    print(e.get())
b = tk.Button(master, text="get", width=10, command=callback)
b.pack()
tk.mainloop()