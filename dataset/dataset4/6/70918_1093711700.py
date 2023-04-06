############### childworkaround.py #################
import os
import subprocess

with open(os.devnull, 'w') as devnull:
    script = "import subprocess; import sys; subprocess.Popen(sys.argv[1:], close_fds=True)"
    proc = subprocess.Popen(['python', '-c', script, 'python', 'resident.py'], stdout=devnull, stderr=devnull, stdin=devnull)