mode = 'a' if not stat.S_ISCHR(os.stat(filename).st_mode) else 'w'
fp = open(filename, mode)