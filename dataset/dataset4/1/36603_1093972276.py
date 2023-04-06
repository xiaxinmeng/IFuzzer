buf = array.array('c', '\000'*256)
ret = fcntl.ioctl(fd, IOCTL_NUMBER, buf)