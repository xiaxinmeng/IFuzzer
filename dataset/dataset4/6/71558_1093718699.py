
import tkinter as tk


def start(root):

    while True:
        root.update()


# tk update loop: mem consumption increases
start(tk.Tk())

# tk mainloop: mem consumption stable
# tk.Tk().mainloop()
