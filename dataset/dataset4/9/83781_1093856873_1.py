import tkinter.ttk
import tkinter.font
frame = tkinter.ttk.Frame()
families=sorted(tkinter.font.families(frame))
for family in families:
    print(family)