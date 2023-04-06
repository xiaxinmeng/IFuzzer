def bogus():
    fd = open('somewhere', 'r').fileno()
    # the file is auto-closed here and fd becomes invalid
    return os.fstat(fd)