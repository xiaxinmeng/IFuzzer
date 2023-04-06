def isomtime(fname):
    """Return file modification time in RFC 3339 (ISO 8601 compliant) format"""
    stamp = time.localtime(os.stat(fname).st_mtime)

    # determine UTC offset rounded to minutes
    # (see http://bugs.python.org/issue7582 for discussion)
    #   true if file was modified during active DST
    isdst = stamp.tm_isdst
    utcoffset = -(time.altzone if (time.daylight and isdst) else time.timezone) // 60