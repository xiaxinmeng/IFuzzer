import tkinter
import locale
import sys

locale.setlocale(locale.LC_NUMERIC, 'de_DE')
class Var(tkinter.DoubleVar):
    def get(self):
        return locale.atof(self._tk.globalgetvar(self._name))

class TestDoubleVar():
    def __init__(self):
        root = tkinter.Tk()
        self.var = Var()
        self.var.set(0.8)
        number = tkinter.Spinbox(
            root,
            from_=0, to=1, increment=0.1,
            textvariable=self.var,
            command=self.update,
            width=4
        )
        number.pack(side=tkinter.LEFT)
        root.mainloop()
    def update(self, *args):
        print(self.var.get())
if __name__ == '__main__':
    TestDoubleVar()