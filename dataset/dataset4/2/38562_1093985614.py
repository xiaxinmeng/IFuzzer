import Tkinter
b = Tkinter.Button(text='Leak',
    command=lambda:b.tk.splitlist('1 2 {3 4} 5 '*10000))
b.pack()
b.mainloop()