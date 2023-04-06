if SOABI:
    so_ext = ''.join(".", SOABI, SO)
else:
    so_ext = SO