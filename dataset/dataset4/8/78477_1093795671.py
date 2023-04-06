if not os.environ.get('XXX_NO_SPEEDUP'):
    from xxx._speedup import somefunc  # Load somefunc from extension
else:
    from xxx._util import somefunc  # Load somefunc from pure Python