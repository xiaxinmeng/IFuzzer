if WINSERVICE:
    _python_exe = os.path.join(sys.exec_prefix, 'python.exe')
else:
    _python_exe = getattr(sys, '_base_executable', sys.executable)