import subprocess
import shlex

for i in range(0, 10000):
    p = subprocess.Popen(shlex.split("ipconfig", posix=False))

    result = p.communicate()