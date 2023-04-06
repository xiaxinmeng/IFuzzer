def _get_xxmodule_path():
    srcdir = sysconfig.get_config_var('srcdir')
    candidates = [
        # use installed copy if available
        os.path.join(os.path.dirname(__file__), 'xxmodule.c'),
        # otherwise try using copy from build directory
        os.path.join(srcdir, 'Modules', 'xxmodule.c'),
        # srcdir mysteriously can be $srcdir/Lib/distutils/tests when
        # this file is run from its parent directory, so walk up the
        # tree to find the real srcdir
        os.path.join(srcdir, '..', '..', '..', 'Modules', 'xxmodule.c'),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path