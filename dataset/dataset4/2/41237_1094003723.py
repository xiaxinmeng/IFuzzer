import Tkinter

text = Tkinter.Text()
text.event_add("<<Up>>", "<Key-Up>")
text.event_add("<<Up>>", "<Key-KP_Up>")
text.bind_class("Text", "<<Up>>", text.bind_class("Text", "<Key-Up>"))
text.pack()
text.mainloop()