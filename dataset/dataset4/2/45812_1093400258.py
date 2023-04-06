import fcntl,os,pty,termios,select,sys,struct,pwd,signal,os
pid,fd=pty.fork()
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH",80,25,0,0))