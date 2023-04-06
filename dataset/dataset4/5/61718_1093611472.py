def _get_default_scheme():
    if os.name == 'posix':
        # the default scheme for posix is posix_prefix
        return 'posix_prefix'
    return os.name