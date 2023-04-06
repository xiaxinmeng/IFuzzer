import os
import threading
os.system(f"grep ^VmRSS /proc/{os.getpid()}/status")
# warmup
for n in range(10):
    timer = threading.Timer(5, None)
    timer.start()
    timer.cancel()
    timer.join()
os.system(f"grep ^VmRSS /proc/{os.getpid()}/status")
for n in range(1000):
    timer = threading.Timer(5, None)
    timer.start()
    timer.cancel()
    timer.join()
os.system(f"grep ^VmRSS /proc/{os.getpid()}/status")