import subprocess
import time

print("Launch started")
program_name = "top"
list = [program_name]
process = subprocess.Popen(list)
while process.poll() == None:
    print("subprocess still running")
    print("Value = " + process.communicate())
    time.sleep(0.1)
    
print("Exit")