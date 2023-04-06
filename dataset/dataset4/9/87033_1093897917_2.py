import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        tk.messagebox.askquestion("Use An Existing File", "Do you want to load and use an existing file?")
        tk.Entry(self.master, width = 20).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.mainloop()