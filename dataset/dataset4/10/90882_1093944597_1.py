with sys.delay_signal_exceptions():
    # Dead simple code, like _before_ we "fixed" it ;-)
    # In particular, while Ctrl-C may terminate the `acquire()` call,
    # KeyboardInterrupt will not be raised until the `with` block
    # exits.
    # Possibly intractable: arranging then for the traceback to
    # point at the code where the exception would have been raised
    # had temporary suspension not been enabled. Then again, since
    # it's not _actually_ raised there at the Python level, maybe
    # it's a Good Thing to ignore.
    if lock.acquire(block, timeout):
        lock.release()
        self._stop()