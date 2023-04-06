def daemonize():
    [...]
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    [...]