def open_noinherit(*args, **kwargs):
    fp = open(*args, **kwargs)
    win32api.SetHandleInformation(msvcrt.get_osfhandle(fp.fileno()),
                                  win32con.HANDLE_FLAG_INHERIT,
                                  0)
    return fp