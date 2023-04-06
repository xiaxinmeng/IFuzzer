# http://stackoverflow.com/a/25678113/819417
def copy(data):
    if not isinstance(data, unicode):
        data = data.decode('mbcs')
    OpenClipboard(None)
    EmptyClipboard()
    hCd = GlobalAlloc(GMEM_DDESHARE, 2 * (len(data) + 1))
    pchData = GlobalLock(hCd)
    wcscpy(ctypes.c_wchar_p(pchData), data)
    GlobalUnlock(hCd)
    SetClipboardData(CF_UNICODETEXT, hCd)
    CloseClipboard()