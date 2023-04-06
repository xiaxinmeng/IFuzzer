def open_noinherit_ctypes(*args, **kwargs):
    HANDLE_FLAG_INHERIT = 1

    import msvcrt
    from ctypes import windll, WinError
    fp = open(*args, **kwargs)
    if not windll.kernel32.SetHandleInformation(msvcrt.get_osfhandle(fp.fileno()), HANDLE_FLAG_INHERIT, 0):
        raise WinError()
    return fp