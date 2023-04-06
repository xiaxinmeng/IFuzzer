
try:
    import tkinter as tk
    import tkinter.messagebox
    from tkinter import font
except:
    import Tkinter as tk
    import tkFont as font

root = tk.Tk()
for name in font.names(root):
    fnt = font.Font(root=root, name=name, exists=True)
    print((name, font.Font.actual(fnt)['family'], fnt['size']))
