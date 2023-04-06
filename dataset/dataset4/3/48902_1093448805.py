from tkinter import Text

text = Text()
print(text.tk.call('info', 'patchlevel'))
text.focus_set()
text.pack()
text.mainloop()