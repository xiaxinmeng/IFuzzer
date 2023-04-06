import os
args=['no_such_executable']
os.execve(args[0], args, os.environ)