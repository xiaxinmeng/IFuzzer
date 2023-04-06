# Active thread administration
_active_limbo_lock = _allocate_lock()
_active = {}    # maps thread id to Thread object
_limbo = {}

def enumerate():
    with _active_limbo_lock:
        return list(_active.values()) + list(_limbo.values())