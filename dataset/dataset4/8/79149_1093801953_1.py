def __del__(self):
    def actual_cleanup_code():
        ...
    loop.call_soon_reentrant_safe(actual_cleanup_code)