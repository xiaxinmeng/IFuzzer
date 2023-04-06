fd = os.open('log', os.O_WRONLY | os.O_CREAT)
print(os.lseek(fd, 1, os.SEEK_SET))
os.write(fd, b'foo')
os.close(fd)