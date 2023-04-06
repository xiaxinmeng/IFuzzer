import subprocess
import time


p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(p.stdout.read(1))   # read 1 byte
print(p.communicate())    # Returns empty output