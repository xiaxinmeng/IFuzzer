if filename:
    file = open(filename, "wb")
    if use_fd:
        file = file.fileno()
else:
    file = None