if followlinks:
    mode = os.stat(path).st_mode
else:
    mode = os.lstat(path).st_mode

if stat.S_ISDIR(mode):
    dirs.append(path)
else:
    nondir.append(path)