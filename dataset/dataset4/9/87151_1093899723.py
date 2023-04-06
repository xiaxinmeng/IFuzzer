def _crash(delay=None):
    """Induces a segfault."""
    if delay:
        time.sleep(delay)
    import faulthandler
    faulthandler.disable()
    faulthandler._sigsegv()