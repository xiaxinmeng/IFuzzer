import os, signal, threading
s = signal.SIGALRM
signal.pthread_sigmask(signal.SIG_BLOCK, [s])
os.kill(os.getpid(), s)
signal.sigwaitinfo([s])
signal.pthread_sigmask(signal.SIG_UNBLOCK, [s])