
import time
import signal


def handle(signum, mask):
    print("received signal at", time.time())


signal.setitimer(signal.ITIMER_REAL, 1, 1)
signal.signal(signal.SIGALRM, handle)

for _ in range(2):
    now = time.time()
    delta = 1 - (time.time() - int(time.time()))
    time.sleep(delta)
    print(now, delta, time.time())
