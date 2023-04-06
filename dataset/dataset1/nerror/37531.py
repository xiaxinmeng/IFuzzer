import sys, subprocess
import os

print("parent pid", os.getpid()),
code = '\n'.join((
    'import datetime, time, sys, subprocess',
    """args = [sys.executable, '-c', 'import time; time.sleep(10); print("done", flush=True)']""",
    'proc = subprocess.Popen(args)',
    'print("child2 pid", proc.pid, file=sys.stderr, flush=True)',
    'while True:',
    '  print(datetime.datetime.now())',
    '  time.sleep(0.1)',
))
args = [sys.executable, '-c', code]
proc = subprocess.Popen(args, stdout=subprocess.PIPE)
print("child1 pid", proc.pid),
try:
    out = proc.communicate(timeout=1.0)
except subprocess.TimeoutExpired:
    print("communicate(): timeout (1)")
else:
    raise Exception("must time out!")

proc.kill()
print("child1 killed")

out = proc.wait(timeout=1.0)
print("wait() returned: returncode", out)

try:
    out = proc.communicate(timeout=1.0)
except subprocess.TimeoutExpired:
    print("communicate() timeout (2)")
else:
    raise Exception("must time out (2)!")

#input("press enter to exit")
