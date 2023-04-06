import atexit

def _tkAtExit():
    if _default_root is not None:
        _default_root.destroy()

atexit.register(_tkAtExit)