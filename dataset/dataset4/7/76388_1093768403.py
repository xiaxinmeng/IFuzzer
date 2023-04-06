import tkinter as tk
root = tk.Tk()

def bad(): print(a, 'bad')
def good(): print('good')

root.after(1000, bad)
root.after(1500, good)
root.mainloop()