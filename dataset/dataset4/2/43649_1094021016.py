import array, fcntl
buf = array.array('B', [0]*1024)
fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
assert any(by != 0 for by in buf)