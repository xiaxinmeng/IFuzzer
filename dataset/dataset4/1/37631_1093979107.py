fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
if fd:
    fnctl.ioctl(fd, tty.TIOCNOTTY, '')
    close(fd)
fcntl.ioctl(slavefd, tty.TIOCSCTTY, '')