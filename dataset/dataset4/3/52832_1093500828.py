def unlink(filename):
    try:
        os.unlink(filename)
    except OSError:
        pass