import subprocess
import signal
subprocess.Popen("/bin/echo", preexec_fn=signal.pause)