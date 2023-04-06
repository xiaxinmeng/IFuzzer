import signal, os

def handler(s, f):
    print("HANDLER", s)

k=signal.SIGRTMIN
signal.signal(k, handler)
signal.pthread_sigmask(signal.SIG_BLOCK, {k})
os.kill(os.getpid(), k)
os.kill(os.getpid(), k)
signal.pthread_sigmask(signal.SIG_UNBLOCK, {k})

