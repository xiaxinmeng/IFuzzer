if isinstance(s, unicode):
    s = unicode.__getslice__(s, None, None)