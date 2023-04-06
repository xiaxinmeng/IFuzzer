def tracefunc(frame, event, arg):
    if frame.f_lineno is None and event != "call":
        raise AssertionError('frame.f_lineno is None!', frame)
    return tracefunc