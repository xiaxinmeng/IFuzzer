import sys
if sys.platform == 'win32':
    # Parses sys.version and deduces the version of the compiler
    import distutils.msvccompiler
    version = distutils.msvccompiler.get_build_version()
    if version is None:
        # This logic works with official builds of Python.
        if sys.version_info < (2, 4):
            clibname = 'msvcrt'
        else:
            clibname = 'msvcr71'
    else:
        if version <= 6:
            clibname = 'msvcrt'
        else:
            clibname = 'msvcr%d' % (version * 10)

    # If python was built with in debug mode
    import imp
    if imp.get_suffixes()[0][0] == '_d.pyd':
        clibname += 'd'

    standard_c_lib = ctypes.cdll.LoadLibrary(clibname+'.dll')