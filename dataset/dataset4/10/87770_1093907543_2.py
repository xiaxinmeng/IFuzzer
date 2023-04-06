
import os
import tempfile
import subprocess as sp

with tempfile.TemporaryNamedPipe() as fifo:
    proc = sp.Popen(["cat", fifo.name], stdout=sp.PIPE, text=True)
    for c in "Kočka leze dírou, pes oknem.":
        print(c, file=fifo)
    proc.wait()

for l in proc.stdout:
    print(l.strip())
