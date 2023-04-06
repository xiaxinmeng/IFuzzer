

def make_var(root):
    return tk.BooleanVar(root, True)

def make_cb(root, v):
    return ttk.Checkbutton(root, text='Checkbutton', variable=v)

if __name__ == '__main__':
    root = tk.Tk()
    v = make_var(root)
    cb = make_cb(root, v)
    cb.pack()
    root.mainloop()
