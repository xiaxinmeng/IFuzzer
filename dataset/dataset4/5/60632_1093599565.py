##################################################
import turtle
square = ((0,0),(0,20),(20,20),(20,0))
turtle.addshape("sq1", square) # sq1 = polygon shape
s = turtle.Shape("compound")
s.addcomponent(square, "red")
turtle.addshape("sq2", s) # sq2 = compound shape
t1 = turtle.Turtle(shape="sq1")
t2 = turtle.Turtle(shape="sq2")
t2.fd(20)
def click(x,y): print("click at",x,y)
t1.onclick(click)
t2.onclick(click)
turtle.mainloop()
##################################################