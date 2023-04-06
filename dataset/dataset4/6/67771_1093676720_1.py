if isinstance(s, unicode):
    s = unicode.__getslice__(s, 0, len(s))