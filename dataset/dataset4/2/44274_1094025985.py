from Tkinter import *
root   = Tk()
canvas = Canvas(root)
text   = "sample text with spaces"
id     = canvas.create_text(0, 0, text=text)

text2  = canvas.itemconfigure(id)['text'][-1]