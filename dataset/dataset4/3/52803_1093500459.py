if sys.platform =='win32':
    distutils.spawn.find_executable(cmd[0]) + cmd[1:]