if 'abortunraisable' in sys._xoptions:
    import signal
    def abort_hook(unraisable,
                   # keep a reference to continue to work
                   # during Python shutdown
                   raise_signal=signal.raise_signal,
                   SIGABRT=signal.SIGABRT):
        raise_signal(SIGABRT)
    sys.unraisablehook = abort_hook