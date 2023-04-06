def rstrips(s, suffix):
    if suffix and s.endswith(suffix):
        s = s[:-len(suffix)]
    return s