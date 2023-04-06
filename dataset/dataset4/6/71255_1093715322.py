launcher = """\
import subprocess, sys
proc = subprocess.Popen(sys.argv)

# Popen object gives up “ownership” of child.
# Caller exits straight afterwards, letting the OS take care of monitoring the child.
proc.detach()
"""

def open_firefox(url):
    cmd = (sys.executable, "-c", launcher, "firefox", url)
    subprocess.check_call(cmd)