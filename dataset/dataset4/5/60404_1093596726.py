import shlex
s = shlex.shlex(r"", posix=False)
s.posix = True
list(s)