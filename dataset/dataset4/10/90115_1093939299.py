
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Exit", command=root.destroy)
button.pack()
root.wm_overrideredirect(True)

root.mainloop()
