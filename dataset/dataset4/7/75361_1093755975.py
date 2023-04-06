import subprocess, sys, os, time

args = [sys.executable, '-c', 'import time; time.sleep(2)']
proc = subprocess.Popen(args)
t0 = time.monotonic()
print("waitpid(0, 0)...")
pid, status = os.waitpid(0, 0)
dt = time.monotonic() - t0
print("%.1f sec later: waitpid(0, 0) -> %s" % (dt, (pid, status)))
proc.wait()