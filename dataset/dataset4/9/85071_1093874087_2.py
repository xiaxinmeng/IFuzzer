if not return_exceptions:
    if fut.cancelled():
        # Check if 'fut' is cancelled first, as
        # 'fut.exception()' will *raise* a CancelledError
        # instead of returning it.
        exc = fut._make_cancelled_error()
        outer.set_exception(exc)
        return