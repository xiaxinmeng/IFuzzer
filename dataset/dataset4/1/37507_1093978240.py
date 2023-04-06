from Tkinter import *
root = Tk()

# If this font is any bigger, it's OK
# If this bd is any smaller, it's OK
t = Text(root, font=("Helvetica", 8, "normal"), bd=16)
# Packing actually makes no difference
t.pack()
# If this string is any shorter, it's OK
t.insert(END, "Hello")
# This see() method SEGVs
t.see(END)

# We never get here
root.mainloop()
# EOF