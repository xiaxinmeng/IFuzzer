import signal
signal.signal(signal.SIGTTOU, signal.SIG_IGN)