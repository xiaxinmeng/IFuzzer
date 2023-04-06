from turtle import Screen, Turtle

screen = Screen()
screen.screensize(800, 800)

# filename = "./Lib/test/imghdrdata/python.gif"
# filename = "./Lib/test/imghdrdata/python.pgm"
# filename = "./Lib/test/imghdrdata/python.ppm"
filename = "./Lib/test/imghdrdata/python.png"

screen.register_shape(filename)
turtle = Turtle(filename)
turtle.penup()
turtle.goto(-280, -280)

screen.mainloop()