import subprocess as subp
import threading
import time


p = subp.Popen(["tr", "[:lower:]", "[:upper:]"],
    stdin=subp.PIPE, stderr=subp.PIPE, stdout=subp.PIPE, close_fds=True)


def read(stdout):
    while True:
        line = stdout.readline()
        if not line: break
        print(line.decode("utf8"))

t = threading.Thread(target=read, args=(p.stdout,))
t.daemon = True
t.start()

p.stdin.write("uppercase\n".encode())
p.stdin.flush()
#p.stdin.close()

time.sleep(1)