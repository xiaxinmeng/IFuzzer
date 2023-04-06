def _python_exit():
    global _shutdown
    with _global_shutdown_lock:
        _shutdown = True
    for executor in list(_executors):
        executor.shutdown()