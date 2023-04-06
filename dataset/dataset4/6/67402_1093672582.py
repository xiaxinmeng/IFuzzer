import subprocess
import sys
script = """import os, time
if not os.fork():  # Child process
    time.sleep(30)
    print("Finally!")
"""
args = (sys.executable, "-c", script)
proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.communicate()
# Hangs for 30 s and then returns (b'Finally!\n', b'')