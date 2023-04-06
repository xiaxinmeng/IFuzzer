def format_exception_chunks(exception):
    return (traceback.TracebackException.from_exception(exception, capture_locals=True).format())