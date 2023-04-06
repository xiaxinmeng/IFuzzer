def _get_xxmodule_path():
    srcdir = sysconfig.get_config_var('srcdir')
    candidates = [
        os.path.join(os.path.dirname(__file__), 'xxmodule.c'),
        os.path.join(srcdir, 'Modules', 'xxmodule.c'),
        os.path.join(srcdir, '..', '..', '..', 'Modules', 'xxmodule.c'),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path