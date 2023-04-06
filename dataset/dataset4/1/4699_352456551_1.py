def lenient_fromisoformat(dtstr):
    # Assuming sep requires a single character be passed, for dates it can be anything
    return datetime.fromisoformat(dtstr, sep=dtstr[10:11] or 'T')