for mode, cbname_args in v.trace_info():
    v.trace_remove(mode, *cbname_args)