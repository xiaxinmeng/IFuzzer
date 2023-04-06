import os
import signal


p = os.getpid()

if os.fork() == 0:
    while True:
        try:
            os.kill(p, signal.SIGCHLD)
        except (ProcessLookupError, KeyboardInterrupt):
            break
    os._exit(0)

qwe = open('qwe.dat', 'w+b')
qwe.seek(2*1024*1024*1024*1024)
qwe.write(b'0')
qwe.flush()
qwe.seek(0)
while True:
    d = qwe.read(65536 * 32)
    if len(d) != 65536 * 32:
        raise Exception('!')