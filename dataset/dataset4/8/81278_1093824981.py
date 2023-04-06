def python_is_optimized():
    """Find if Python was built with optimizations."""
    cflags = sysconfig.get_config_var('PY_CFLAGS') or ''
    final_opt = ""
    for opt in cflags.split():
        if opt.startswith('-O'):
            final_opt = opt
    return final_opt not in ('', '-O0', '-Og')