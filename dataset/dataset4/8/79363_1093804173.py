import subprocess

child = subprocess.Popen(
    ['/usr/local/bin/python3.7', '-c', 'import os, time; os.close(1), time.sleep(30)'],
    stdout=subprocess.PIPE,
)

while True:
    try:
        child.communicate(timeout=3)
        break
    except subprocess.TimeoutExpired:
        # do something useful here
        pass