from tkinter import Label, Tk
from tkinter.simpledialog import Dialog


class CalendarDialog(Dialog):
    def __init__(self, parent, title='', year=0, month=0):
        self.year = year  # type: int
        self.month = month  # type: int

        Dialog.__init__(self, parent, 'Select a date')

    def body(self, parent):
        Label(parent, text='A label').pack()


master = Tk()
result = CalendarDialog(master, year=2017, month=9).result
master.mainloop()