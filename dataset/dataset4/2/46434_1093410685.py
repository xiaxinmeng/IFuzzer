def myfunc():
    f = open('somewhere', 'r')
    fd = f.fileno()
    return os.fstat(fd)