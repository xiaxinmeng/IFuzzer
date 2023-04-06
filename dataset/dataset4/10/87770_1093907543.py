
import os
import tempfile
import subprocess as sp

fifo_path = tempfile.mktemp()
os.mkfifo(fifo_path, 0o600)
try:
    proc = sp.Popen(["cat", fifo_path], stdout=sp.PIPE, text=True)
    with open(fifo_path, "w") as fifo:
        for c in "Kočka leze dírou, pes oknem.":
            print(c, file=fifo)
    proc.wait()
finally:
    os.unlink(fifo_path)

for l in proc.stdout:
    print(l.strip())
