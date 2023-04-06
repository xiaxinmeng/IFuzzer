def should_flush_before_close(handler):
    if callable(getattr(handler, 'shouldFlushBeforeClose', None)):
        return handler.shouldFlushBeforeClose()
    return True