
import tkinter as tk

hmr = tk.Tk()
hmr.attributes('-alpha', 0)
hmr.withdraw()

root = tk.Toplevel(class_='toplevel')
root.attributes('-alpha', 0)

root.title('My Test Title')

frame = tk.Frame(root)
frame.pack(side=tk.TOP, anchor='nw', padx=0, pady=0, expand=False, fill=tk.NONE)
a = tk.Label(frame, text ="Hello World")


a.pack()

b = tk.Button(frame, text="QUIT", command=frame.quit)
b.pack()

root.update_idletasks()
root.geometry("+600+600")
root.update_idletasks()
root.attributes('-alpha', 1)

root.mainloop()
