if self._is_gcc(compiler):
    # gcc on non-GNU systems does not need -Wl, but can
    # use it anyway.  Since distutils has always passed in
    # -Wl whenever gcc was used in the past it is probably
    # safest to keep doing so.
    if sysconfig.get_config_var("GNULD") == "yes":
        # GNU ld needs an extra option to get a RUNPATH
        # instead of just an RPATH.
        return "-Wl,--enable-new-dtags,-R" + dir
    else:
        return "-Wl,-R" + dir
else:
    # No idea how --enable-new-dtags would be passed on to
    # ld if this system was using GNU ld.  Don't know if a
    # system like this even exists.
    return "-R" + dir