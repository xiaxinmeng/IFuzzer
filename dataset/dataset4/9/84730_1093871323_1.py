
import subprocess
import time

proc = subprocess.Popen(["sh", "-c", "exit 0"])

time.sleep(5)

proc.terminate()
