import subprocess

for _ in xrange(2):
    stdout = open("stdout.txt", "w")
    try:
        p = subprocess.Popen(["unknown"], stdout=stdout)
    except WindowsError:
        pass