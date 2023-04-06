import os, sys
args = [sys.executable, "-c", "pass"]
os.execve(args[0], args, os.environb)