class URLopener:
    """Class to open URLs.
    This is a class rather than just a subroutine 
because we may need
    more than one set of global protocol-specific 
options.
    Note -- this is a base class for those who don't 
want the
    automatic handling of errors type 302 (relocated) 
and 401
    (authorization needed)."""

    __tempfiles = None

    version = "Python-urllib/%s" % __version__

    # Constructor
    def __init__(self, proxies=None, **x509):
        if proxies is None:
            proxies = {}
            # proxies = getproxies()