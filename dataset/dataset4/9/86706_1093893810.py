
import os
import time
import subprocess

def daemon():
    pid = os.fork()
    if pid != 0:
        subprocess.run(["lldb", '-p', str(pid)])
        time.sleep(10)
        os._exit(0)
    time.sleep(1)

daemon()
