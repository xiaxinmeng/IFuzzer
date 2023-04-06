import Tkinter

text = Tkinter.Text()
text.pack()
text.insert('1.0',
        'class C:\n\tdef m(self, c):\n                '
        'if c:\n                        c = False\n'
        '\t\t\tc = False\n                else:\n        '
        '\t\tc = True\n\t\tc = True\n')
text.mainloop()