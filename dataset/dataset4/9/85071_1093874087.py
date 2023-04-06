if outer._cancel_requested:
    # If gather is being cancelled we must propagate the
    # cancellation regardless of *return_exceptions* argument.
    # See issue 32684.
    exc = fut._make_cancelled_error()
    outer.set_exception(exc)