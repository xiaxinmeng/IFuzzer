def keep_argv(module, argv):
    return argv

def set_argv0(module, argv):
    return module.__file__ + argv[1:]

def set_argv(argv, *, implicit_argv0=True):
    argv_override = list(argv)
    if implicit_argv0:
        def _set_argv(module, original_argv):
            return [module.__file__] + argv_override
    else:
        def _set_argv(module, original_argv):
            return argv_override
    return _set_argv