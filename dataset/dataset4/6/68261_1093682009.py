import sys
import os

sys.stdout.write("%s\n" % sys.stdin.mode)
sys.stdout.flush()
f = os.fdopen(sys.stdin.fileno(), "r")
f.write("aaaa")
f.flush()
f.read()
f.close()