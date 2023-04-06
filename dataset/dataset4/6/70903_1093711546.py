import fcntl
import signal
import os


def handle_alarm(signum, frame):
    print("Received alarm in process {}!".format(os.getpid()))


child = os.fork()
if child:
    signal.signal(signal.SIGALRM, handle_alarm)
    signal.alarm(1)
    with open("foo", "w") as f:
        print("Locking in process {}...".format(os.getpid()))
        fcntl.flock(f, fcntl.LOCK_EX)
        print("Locked in process {}.".format(os.getpid()))
        os.waitpid(child, 0)
else:
    signal.signal(signal.SIGALRM, handle_alarm)
    signal.alarm(1)
    with open("foo", "w") as f:
        print("Locking in process {}...".format(os.getpid()))
        fcntl.flock(f, fcntl.LOCK_EX)
        print("Locked in process {}.".format(os.getpid()))