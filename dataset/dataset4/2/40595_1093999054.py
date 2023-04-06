def ensure_relative (path):
    """Take the full path 'path', and make it a relative path so
    it can be the second argument to os.path.join().
    """
    drive, path = os.path.splitdrive(path)
    if sys.platform == 'mac':
        return os.sep + path
    else:
        if path[0:1] == os.sep:
            path = drive + path[1:]
        return path