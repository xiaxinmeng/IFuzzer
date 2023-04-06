import turtle

s = turtle.Screen()

def changecolor():
    s.bgcolor(1.0, 0.5)  # needs 3 floats as arguments

s.ontimer(changecolor, 1000)
turtle.mainloop()