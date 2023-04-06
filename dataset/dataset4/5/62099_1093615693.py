while True:
    try:
        listdir(0)
    except NotADirectoryError:
        pass