import tkinter
from tkinter import ttk

master = tkinter.Tk()
_out1Value = tkinter.IntVar(master)
out1Slider = ttk.LabeledScale(master, from_=-100, to=100, variable=_out1Value, compound="bottom")
_out1Value.set(0)