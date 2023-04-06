fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
tty = os.fdopen(fd, 'w+', 1)