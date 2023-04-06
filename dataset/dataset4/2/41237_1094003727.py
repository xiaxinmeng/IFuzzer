import Tkinter

def my_up(event):
    widget = event.widget
    if event.keysym == 'KP_Up' and event.state & 16:
        widget.tk.call('tk::TextInsert', widget, event.char)
        return "break"
    pos = widget.tk.call('tk::TextUpDownLine', widget, -1)
    widget.tk.call('tk::TextSetCursor', widget, pos)

text = Tkinter.Text()
text.event_add("<<Up>>", "<Key-Up>")
text.event_add("<<Up>>", "<Key-KP_Up>")
text.bind_class("Text", "<<Up>>", my_up)
text.pack()
text.mainloop()