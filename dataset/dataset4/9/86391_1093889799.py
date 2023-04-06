from tkinter import Tk
from tkinter.scrolledtext import ScrolledText
root = Tk()
text = ScrolledText(root, width=80, height=40)
text.pack()

for i in range(0x10000, 0x40000, 32):
    chars = ''.join(chr(i+j) for j in range(32))
    text.insert('insert', f"{hex(i)} {chars}\n")

input("Press enter to exit")