import os

cmdline=["/usr/bin/printenv"]
env={'a=b': 'c'}
os.execve(cmdline[0], cmdline, env)
# this prints a=b=c