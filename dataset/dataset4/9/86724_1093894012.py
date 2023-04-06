
import os
import subprocess
import time

child = subprocess.Popen(["true"])
time.sleep(1)
child.kill()
os.waitpid(child.pid, 0)
