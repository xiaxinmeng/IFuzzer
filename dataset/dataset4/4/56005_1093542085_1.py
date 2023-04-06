def __gf__(_it=iter_exp):
    for loop_var in _it:
        yield result_exp(loop_var)
ge = __gf__()
del __gf__