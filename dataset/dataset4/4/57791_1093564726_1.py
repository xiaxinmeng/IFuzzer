if sys.__stderr__ is None:
    sys.__stderr__ = ErrorNotify()

if sys.stderr is None:
    sys.stderr = ErrorNotify()

if sys.__stdout__ is None:
    sys.__stdout__ = ErrorNotify(devnull=True)

if sys.stdout is None:
    sys.stdout = ErrorNotify(devnull=True)

sys.__stderr__ = ErrorNotify()
sys.stderr = ErrorNotify()