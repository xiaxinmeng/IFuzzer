
def mktemp(suffix='', prefix='tmp', dir=None):
    if dir is None:
        dir = gettempdir()
    return _os.path.join(dir, prefix + secrets.token_urlsafe(ENTROPY_BYTES) + suffix)
