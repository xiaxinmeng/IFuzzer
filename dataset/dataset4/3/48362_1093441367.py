import subprocess, sys

p1 = subprocess.Popen("cat", bufsize=0, stdin=subprocess.PIPE)
p2 = subprocess.Popen("cat", bufsize=0, stdin=subprocess.PIPE)

p1.stdin.close()
ret = p1.wait()
print >>sys.stderr, "Child 1 wait completed with ret", ret

p2.stdin.close()
ret = p2.wait()
print >>sys.stderr, "Child 2 wait completed with ret", ret, "Bye bye"