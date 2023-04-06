from tkinter import *
tk = Tk()
bv = BooleanVar()
print(bv.get(), type(bv.get()))
bv.set(True)
print(bv.get(), type(bv.get()))
bv.set(False)
print(bv.get(), type(bv.get()))