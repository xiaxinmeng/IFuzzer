_is_shutdown = False

def _on_shutdown():
    global _is_shutdown
    _is_shutdown = True

atexit.register(_on_shutdown)