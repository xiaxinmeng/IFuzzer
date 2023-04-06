from signal import *
import subprocess

signum = SIGCHLD
process = subprocess.Popen("sleep 1", shell=True)
print("Wait %s..." % signum)
pthread_sigmask(SIG_BLOCK, [signum])
sigwait([signum])
pthread_sigmask(SIG_UNBLOCK, [signum])
print("done")
process.wait()