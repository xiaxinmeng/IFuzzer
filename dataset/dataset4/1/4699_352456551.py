def strict_fromisoformat(dtstr, sep='T'):
    if dtstr[10:11] != sep:
        raise ValueError('Invalid isoformat string: %s' % dstr)
    return datetime.fromisoformat(dtstr)