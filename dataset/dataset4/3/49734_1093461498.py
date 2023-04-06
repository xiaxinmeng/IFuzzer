import win32process
win32process.CreateProcess(None, 'f(o.bat', None, None, 1, 0, None,
None, win32process.STARTUPINFO())