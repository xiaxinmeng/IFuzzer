def _iter_chain(exc, custom_tb=None, seen=None):
    if seen is None:
        seen = set()
    seen.add(exc)
    its = []
    context = exc.__context__