def zinfo_from_file(fullname, arcname):
    st = os.stat(fullname)
    mtime = time.localtime(st.st_mtime)
    date_time = mtime[0:6]
    if date_time[0] < 1980:
        date_time = (1980, 1, 1, 0, 0, 0)
    zinfo = zipfile.ZipInfo(arcname, date_time)
    return zinfo