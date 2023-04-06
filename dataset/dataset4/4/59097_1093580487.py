import termios
lflags = termios.tcgetattr(0)[3]
print (lflags & termios.TOSTOP) != 0