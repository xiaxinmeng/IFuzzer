def _enumerate():
    """Internal use only: enumerate() without the lock."""
    return _active.values() + _limbo.values()