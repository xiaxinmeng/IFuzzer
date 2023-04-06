new = termios.tcgetattr(fd)
new[3] = new[3] & ~termios.ECHO          # lflags