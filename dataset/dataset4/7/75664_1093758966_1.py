label = ttk.Label(app, text='test')
label.pack()
label.bind('<Button-1>', down)
label.bind('<ButtonRelease-1>', up)