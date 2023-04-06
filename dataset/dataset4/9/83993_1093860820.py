
_threading_atexits = None

def register_atexit(func, *args, **kwargs):
    global _threading_atexits
    if _threading_atexits is None:
        _threading_atexits = []
    call = functools.partial(func, *args, **kwargs)
    _threading_atexits.append(call)

# [snip]

def _shutdown():
    if _main_thread._is_stopped:
        # _shutdown() was already called
        return

    # Main thread
    tlock = _main_thread._tstate_lock
    # The main thread isn't finished yet, so its thread state lock can't have
    # been released.
    assert tlock is not None
    assert tlock.locked()
    tlock.release()
    _main_thread._stop()
    
    # Call registered threading atexit functions
    for atexit_call in _threading_atexits:
        atexit_call()

    # Join all non-deamon threads
    # [snip]
