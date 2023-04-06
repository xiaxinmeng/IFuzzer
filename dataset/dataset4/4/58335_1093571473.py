atime = os.stat(path).st_atime_ns
mtime = os.stat(path).st_mtime_ns
os.utime(path, (atime, mtime), resolution="ns")