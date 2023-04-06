def opener_noinherit(filename, flags):
    return os.open(filename, flags | os.O_NOINHERIT)
f = open(filename, opener=opener_noinherit)