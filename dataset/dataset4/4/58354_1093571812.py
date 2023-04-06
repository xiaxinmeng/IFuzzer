from tkinter import *
main = Tk()
text = Text(main, width=40, height=10, wrap="char")
text.pack()
text.insert(INSERT, "".join(map(str, range(100))))
text.tag_add(SEL, "1.0", "end")
text.focus_set()
def jump():
    text.after(500, btn.focus_set)
    text.after(1000, text.focus_set)
btn = Button(main, text="Click me", command=jump)
btn.pack()
main.mainloop()