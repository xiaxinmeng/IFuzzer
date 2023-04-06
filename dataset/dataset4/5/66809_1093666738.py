def _extract_tb_or_stack_iter(curr, limit, extractor):
    # Distinguish frames from tracebacks (need to import types)
    if limit is None:
        limit = getattr(sys, 'tracebacklimit', None)
    elif limit < 0 and isinstance(curr, types.TracebackType):
        seq = list(_extract_tb_or_stack_iter(curr, None, extractor))
        yield from seq[limit:]
    else:
        pass