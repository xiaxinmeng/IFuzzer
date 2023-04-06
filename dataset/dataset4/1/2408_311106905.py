
import os
import signal
import time

sigs = []

def handler1(signum, frame):
    os.kill(os.getpid(), signal.SIGPROF)

def handler2(signum, frame):
    signal.setitimer(signal.ITIMER_REAL, 1e-6)

def handler_itimer_real(signum=None, frame=None):
    sigs.append(signum)


if __name__ == "__main__":
    N = 10
    signal.signal(signal.SIGIO, handler1)
    signal.signal(signal.SIGPROF, handler2)
    signal.signal(signal.SIGALRM, handler_itimer_real)
    for i in range(N):
        os.kill(os.getpid(), signal.SIGIO)
        for j in range(3):
            time.sleep(1e-3)

    print("sigs =", len(sigs), sigs)
