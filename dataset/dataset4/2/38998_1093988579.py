import Tkinter as Tk
Lb = None

def update_lb ():
    global Lb    
    Lb.delete(0, Tk.END)

    for ii in range(100):
        Lb.insert(Tk.END, 'Item %d' % ii)
        Lb.itemconfigure(ii, bg='red')

    Lb.after(10, update_lb)


root = Tk.Tk()
Lb = Tk.Listbox(root)
Lb.pack()
Lb.after(1000, update_lb)
root.mainloop()