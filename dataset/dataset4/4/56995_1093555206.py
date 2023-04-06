import subprocess

proc1 = subprocess.Popen(['cat'], stdin=subprocess.PIPE)
proc2 = subprocess.Popen(['cat'], stdin=subprocess.PIPE)

proc1.stdin.close()
proc1.wait()