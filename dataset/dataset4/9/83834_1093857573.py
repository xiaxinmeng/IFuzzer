import os
args=['no_such_executable']
os.execvpe(args[0], args, os.environ)