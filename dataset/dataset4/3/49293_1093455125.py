def get_msvcr():
    """Include the appropriate MSVC runtime library if Python was built
    with MSVC 7.0 or later.
    """
    msc_pos = sys.version.find('MSC v.')
    if msc_pos != -1:
        msc_ver = sys.version[msc_pos+6:msc_pos+10]
        if msc_ver == '1300':
            # MSVC 7.0
            return ['msvcr70']
        elif msc_ver == '1310':
            # MSVC 7.1
            return ['msvcr71']
        elif msc_ver == '1400':
            # VS2005 / MSVC 8.0
            return ['msvcr80']
        elif msc_ver == '1500':
            # VS2008 / MSVC 9.0
            return ['msvcr90']
        else:
            raise ValueError("Unknown MS Compiler version %i " % msc_Ver)