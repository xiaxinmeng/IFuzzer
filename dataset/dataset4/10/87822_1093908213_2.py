def format_exception_chunks(exception):
    try:
        tbe = (traceback.TracebackException
               . from_exception(exception, capture_locals=True))
        return tbe.format()
    except Exception:
        pass
    # the traceback module fails to catch exceptions that occur when
    # formatting local variables' values, so we retry without
    # requesting the local variables.
    try:
        tbe = traceback.TracebackException.from_exception(exception)
        return ('WARNING: Exceptions were raised while trying to'
                ' format exception traceback with local variable'
                ' values,\n'
                'so the exception traceback was formatted without'
                ' local variable values.\n',
                *tbe.format())
    except Exception:
        return ('WARNING: Exceptions were raised while trying to format'
                ' exception traceback,\n'
                'so no formatted traceback information is being'
                ' provided.\n',)