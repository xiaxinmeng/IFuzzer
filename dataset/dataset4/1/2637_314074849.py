if host_platform == 'darwin':
    os_release = int(os.uname()[2].split('.')[0])
    dep_target = sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET')
    if (dep_target and
            (tuple(int(n) for n in dep_target.split('.')[0:2])
                < (10, 5) ) ): 
        os_release = 8
    if os_release < 9: 
        # MacOSX 10.4 has a broken readline. Don't try to build
        # the readline module unless the user has installed a fixed
        # readline package
        if find_file('readline/rlconf.h', inc_dirs, []) is None: