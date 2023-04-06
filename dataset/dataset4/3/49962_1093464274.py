from Tkinter import *
import tkFileDialog

master = Tk()
master.withdraw() #hiding tkinter window

Inputfiles = tkFileDialog.askopenfilenames(title="Select the source input file(s)", filetypes=[("mpf file",".mpf"),("All files",".*")])

#Heres the TRICK!
InputfilesList =  master.tk.splitlist(Inputfiles)