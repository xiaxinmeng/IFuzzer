#!/usr/bin/env python3
import tkinter as tk


class NodePopup(tk.Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=0)

        self.send_disabled = tk.BooleanVar()

        self.add_checkbutton(label="Disable sending",
                             variable=self.send_disabled, command=self.toggle_send)

    def popup(self, event):
        print('send_disabled before:', self.send_disabled.get())
        self.post(event.x_root, event.y_root)

    def toggle_send(self):
        print('send_disabled after:', self.send_disabled.get())


def change():
    state = not menu.send_disabled.get()
    menu.send_disabled.set(state)

root = tk.Tk()
root.pack_propagate(0)

menu = NodePopup(root)
root.bind('<Button-2>', menu.popup)

root.mainloop()