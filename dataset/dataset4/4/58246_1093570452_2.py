def _get_xxmodule_path():
    if sysconfig.is_python_build():
        srcdir = sysconfig.get_config_var('projectbase')
        path = os.path.join(os.getcwd(), srcdir, 'Modules', 'xxmodule.c')
    else:
        os.path.join(os.path.dirname(__file__), 'xxmodule.c')
    if os.path.exists(path):
        return path