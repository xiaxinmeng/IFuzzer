tree = ttk.Treeview(root)
tree.tag_configure('RED_TAG', foreground='red', font=('arial', 12))
tree.insert('', tk.END, text='Black line')
tree.insert('', tk.END, text='Red line', tag='RED_TAG')
tree.pack()

root.mainloop()