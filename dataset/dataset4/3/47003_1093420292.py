import Tkinter

root = Tkinter.Tk()

text = Tkinter.Text()
text.focus_set()
vbar = Tkinter.Scrollbar(orient='vertical', command=text.yview)
text.configure(yscrollcommand=vbar.set)

vbar.pack(side='right', fill='y')
text.pack(fill='both', expand=True)

for l in range(int(text['height']) + 10):
    text.insert('end', "x\n")

root.mainloop()