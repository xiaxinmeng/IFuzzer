for root, dirnames, filenames in Path().walk(follow_symlinks=False):
    for name in dirnames + filenames:
        path = root / name
        if path.is_dir():
            pass # do things to directory, or symlink to directory.