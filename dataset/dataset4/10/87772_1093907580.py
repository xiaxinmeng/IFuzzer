# t8.py
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Your first App')

        first_label = tk.Label(self, text = "I'm a cool App!!", font=10, bg="black",fg="red" )
        first_label.pack(pady= 2, padx = 2)

app = Application()
app.mainloop()