s = ttk.Style()
s.element_options('Button.label')
('-compound', '-space', '-text', '-font', '-foreground', '-underline',
'-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image',
'-stipple', '-background')
s.configure('TButton', font='helvetica 24')
{}
b = ttk.Button(root)
b.configure(text='blah')