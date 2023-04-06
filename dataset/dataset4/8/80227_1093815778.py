import subprocess
subprocess.Popen(["/usr/bin/id"], user=1000, group=1000).wait()