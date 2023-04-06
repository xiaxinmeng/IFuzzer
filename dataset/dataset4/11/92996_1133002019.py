import tkinter as tk

def window_size_up(event):
    width_window = root.winfo_width() + 20
    root.geometry(f'{width_window}x{width_window}')

def window_size_down(event):
    width_window = root.winfo_width() - 20
    root.geometry(f'{width_window}x{width_window}')


root = tk.Tk()
root.minsize(250, 250)
# root.maxsize(1900, 1900)  # Uncomment for bug.
root.resizable(width=False, height=False)
root.bind_all("<Button-4>", window_size_up)
root.bind_all("<Button-5>", window_size_down)
root.mainloop()