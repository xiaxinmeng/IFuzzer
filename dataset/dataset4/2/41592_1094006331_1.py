import win32con
p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
creationflags=win32con.CREATE_NO_WINDOW)