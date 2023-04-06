def _searchbases(cls, accum):
    # Simulate the "classic class" search order.
    if cls in accum:
        return
    if not hasattr(cls, "__bases__"): #Additional code.
        return
    accum.append(cls)
    for base in cls.__bases__:
        _searchbases(base, accum)