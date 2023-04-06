def _get_source_filename():
    srcdir = sysconfig.get_config_var('srcdir')
    return os.path.join(srcdir, 'Modules', 'xxmodule.c')