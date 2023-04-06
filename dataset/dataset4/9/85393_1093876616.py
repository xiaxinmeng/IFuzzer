import signal
import subprocess
import sys

CHILD_PROCESS = '''
import signal, sys
signal.signal(signal.SIGINT, lambda *x: None)
written = sys.stdout.write('x' * 16777216)
print('written:', written, file=sys.stderr, flush=True)
'''

proc = subprocess.Popen(
    [sys.executable, '-u', '-c', CHILD_PROCESS],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
read = len(proc.stdout.read(1))
proc.send_signal(signal.SIGINT)
read += len(proc.stdout.read())
stdout, stderr = proc.communicate()
assert stdout == b''
print('stderr:', stderr)
assert read == 16777216, "read: {}".format(read)