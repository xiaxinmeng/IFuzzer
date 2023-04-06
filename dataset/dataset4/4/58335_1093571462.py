st = os.stat(src)
atime = (math.floor(st.st_atime), st.st_atime_ns)
mtime = (math.floor(st.st_mtime), st.st_mtime_ns)
os.utime(dst, (atime, mtime))