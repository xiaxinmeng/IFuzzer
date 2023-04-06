import tracemalloc; tracemalloc.start()
import subprocess, gc

def func(loops) :
    for x in range(loops):
        proc = subprocess.Popen(['true'])
        with proc:
            proc.wait()

# warmup
func(10)