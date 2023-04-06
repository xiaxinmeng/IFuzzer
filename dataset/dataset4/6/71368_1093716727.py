def gmean(a, axis=0):
    a, axis = _chk_asarray(a, axis)
    log_a = ma.log(a)
    return ma.exp(log_a.mean(axis=axis))