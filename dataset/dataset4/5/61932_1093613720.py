if sys.prefix == sys.base_prefix:
    # not in venv
    ignore_options = []
else:
    # in venv
    ignore_options = ['install-base', ...]