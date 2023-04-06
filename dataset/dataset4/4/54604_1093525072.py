def commondirname(paths):
    subpath = os.path.commonprefix(paths)
    for path in paths:
        if path == subpath:
            return subpath
    else:
        return os.path.join(os.path.split(subpath)[0], "")