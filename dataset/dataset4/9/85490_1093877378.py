def some_logger(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        try:
            # Unfortunately this code hit RecursionError and catched it
            logger.info(some_message)
        except Exception as e:
            pass # Avoid affecting user function
        return func(*args, **kwargs)
    return new_func