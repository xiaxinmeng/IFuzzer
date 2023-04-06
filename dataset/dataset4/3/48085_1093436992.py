import threading
import Tkinter

lbl = Tkinter.Label(text="hi")
threading.Thread(target=lambda: lbl.configure(text="hi there")).start()
lbl.mainloop()