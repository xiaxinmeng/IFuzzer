import Tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kw):
        tk.Tk.__init__(self, *args, **kw)
        
        self.entry = tk.Entry(self)
        self.entry.grid(padx=20, pady=20)
        self.entry.focus_set()
        self.entry.bind("<FocusOut>", self.entry_focus_lost)
        
        self.menubar = tk.Menu(self)
        self["menu"] = self.menubar
        
        self.menufile = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(menu=self.menufile, label="File")

    def entry_focus_lost(self, event):
        widget_with_focus = self.focus_get()


app = App()
app.mainloop()