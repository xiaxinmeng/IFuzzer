import tkinter as tk
r = tk.Tk()
v = tk.StringVar(r)
def c(*args): print("hello", args)
print(v.trace_add('write', c))
print(v.trace_add('write', c))
v.set('a')