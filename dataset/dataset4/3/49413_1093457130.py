import Tkinter

def insert():
    text.insert('end', 'buh\n')
    text.see('end')
    text.after(100, insert)

text = Tkinter.Text()
text.pack(expand=True, fill='both', side='left')
vbar = Tkinter.Scrollbar(orient='vertical', command=text.yview)
vbar.pack(side='right', fill='y')
text.configure(yscrollcommand=vbar.set)
text.after(100, insert)

text.mainloop()