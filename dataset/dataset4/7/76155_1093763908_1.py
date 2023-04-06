import tkinter as tk
root = tk.Tk()
text = tk.Text(root)
sample = '''
<replace this with sample that allows reported error>
'''
text.insert('1.0', sample)
text.pack()
root.mainloop()