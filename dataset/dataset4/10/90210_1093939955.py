import tkinter as tk
r = tk.Tk()
t = tk.Text(r)
t.pack()

def keyevent(e):
    if c := e.char:
        print(f'char: {c}, ord: {ord(c)}, ', end='')
    print(f'code: {e.keycode}, sym: {e.keysym}, num: {e.keysym_num}.')
t.bind('<Key>', keyevent)