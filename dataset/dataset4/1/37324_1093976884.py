# test posixmodule.popen(), 
# would need check around line 2835
# as first code in popen()
import posix
# you may need a command that works, 
# I'm guessing cmd.exe is ok
posix.popen('cmd.exe', '.zip')

# test socketmodule.sock_makefile(), 
# would need check around line 1572
# after PyArg_ParseTuple
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.makefile('.zip')