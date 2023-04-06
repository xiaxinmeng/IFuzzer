def new_isoformat(dtstr):
    if len(dtstr) > 10 and is_surrogate(dtstr[10]):
        dtstr = "%sT%s" % (dtstr[0:10], dtstr[11:])
    return old_isoformat_minus_segfaults(dtstr)