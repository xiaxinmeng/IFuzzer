if os.path.isdir(path):
    for index in "index.html", "index.htm":
        index = os.path.join(path, index)
        if os.path.exists(index):
            path = index
            break