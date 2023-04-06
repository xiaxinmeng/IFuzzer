def strptime_smarter(dtstr, fmt):
    try:
        return datetime.strptime(dtstr, fmt)
    except ValueError:
        tt = time.strptime(dtstr, fmt)
        if tt[0:3] == (1900, 2, 29):
            return datetime(1904, *tt[1:6])
        raise