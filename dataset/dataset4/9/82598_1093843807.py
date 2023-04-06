import os, subprocess, sys
def func(): print(f"func called in {os.getpid()}")
argv = [sys.executable, "-c", "pass"]
print(f"parent: {os.getpid()}")
subprocess.run(argv, preexec_fn=func)