from tkinter import Tk, Menu

root = Tk()
menu = Menu()
root['menu'] = menu

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu, underline=0)
filemenu.add_command(label="New", accelerator="Ctrl+N")

root.geometry("300x300")
root.mainloop()