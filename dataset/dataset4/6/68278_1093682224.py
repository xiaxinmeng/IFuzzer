from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(str(v))
r.destroy()