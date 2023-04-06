import signal
signals = [s for s in dir(signal) if s.startswith("SIG")]
max([(getattr(signal, s), s) for s in signals])
(64, 'SIGRTMAX')
signal.NSIG
