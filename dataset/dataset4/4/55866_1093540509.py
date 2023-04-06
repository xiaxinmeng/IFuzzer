for i in range(4, 256):
    os.dup2(1, i)