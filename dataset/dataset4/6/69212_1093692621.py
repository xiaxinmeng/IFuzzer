def mkdtemp_persistent(*args, persistent=True, **kwargs):
    if persistent:
        @contextmanager
        def normal_mkdtemp():
            yield tempfile.mkdtemp()
        return normal_mkdtemp(*args, **kwargs)
    else:
        return tempfile.TemporaryDirectory(*args, **kwargs)

with mkdtemp_persistent(persistent=False) as dir:
    ...