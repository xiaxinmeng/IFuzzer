import matplotlib.pyplot as plt
import tkinter as tk

plt.set_cmap('viridis') # <--- when placed here, breaks the variable
root = tk.Tk()
#plt.set_cmap('viridis') # <--- when placed here, everything is fine

# creation of variable class and widget
var = tk.BooleanVar()
tk.Checkbutton(root, variable=var).pack()

# for printing result
def on_click():
    print(var.get())
tk.Button(root, text="Print State to Console", command=on_click).pack()

root.mainloop()