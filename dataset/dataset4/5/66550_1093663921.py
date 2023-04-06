import tkinter as tk
root = tk.Tk()
text = tk.Text(root)
text.pack()
text.insert('insert', 'a\tb')
text.tag_add('TAB', 1.1, 1.2)
text.tag_config('TAB', background='#ffd')  # light yellow, or
text.tag_config('TAB', background='#eee')  # light gray