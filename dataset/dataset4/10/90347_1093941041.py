import tkinter

def change_color():
    canvas.itemconfig(text, fill="red")

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()

text = canvas.create_text((200, 200), text="f", font=("Times New Roman", 200), fill="black")

button = tkinter.Button(text="Change Color", command=change_color)
button.pack()

root.mainloop()