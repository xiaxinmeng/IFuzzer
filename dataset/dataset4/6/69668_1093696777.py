import signal

def sighandler(signum, frame):
    raise InterruptedError

signal.signal(signal.SIGWINCH, sighandler)