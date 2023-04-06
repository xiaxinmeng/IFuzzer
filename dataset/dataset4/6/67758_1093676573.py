import subprocess, sys

args = [sys.executable, '-c', 'pass']
proc = subprocess.Popen(args, stdin=subprocess.PIPE)
try:
    with proc:
        proc.stdin.write(b'x' * (2**20))
except BrokenPipeError:
    pass
print("is proc stdin closed?", proc.stdin.closed)