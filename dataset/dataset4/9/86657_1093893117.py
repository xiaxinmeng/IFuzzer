import threading
import tkinter as tk
def create_tp():
    t = tk.Toplevel()
    t.wait_visibility()
root = tk.Tk()
tk.Button(root, text="Create", command=lambda:
          threading.Thread(target=create_tp).start()).pack()
root.mainloop()