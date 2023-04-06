# BEGIN
import signal, sys
import subprocess

def handler(sig, frames):
    raise RuntimeError("Alarm!")

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
b = sys.stdin.buffer.raw.readall()
print(len(b))
signal.alarm(0)
#END