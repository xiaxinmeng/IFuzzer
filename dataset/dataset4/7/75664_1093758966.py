def down(event): print('down')
def up(event): print('up')

app = tk.Tk()
app.bind('<Button-1>', down)
app.bind('<ButtonRelease-1>', up)
app.mainloop()