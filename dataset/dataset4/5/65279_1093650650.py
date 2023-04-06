import subprocess
ls = subprocess.Popen(["ls", "-1"], stdout=subprocess.PIPE)
wc = subprocess.Popen(["wc", "-l"], stdin=ls.stdout)
ls.wait()
wc.wait()