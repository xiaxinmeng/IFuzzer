if sys.version_info < (3,):
    try:
        import readline, os, atexit
        histfile = os.path.join(os.path.expanduser("~"), ".python2_history")
        try:
            readline.read_history_file(histfile)
        except IOError:
            pass
        atexit.register(readline.write_history_file, histfile)
        del os, histfile
    except ImportError:
        pass