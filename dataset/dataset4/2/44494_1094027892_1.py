class loggingwrapper(object):
    __slots__ = ['socketinfo']
    def __init__(self, socketinfo):
        self.socketinfo = str(socketinfo)
    def __getattr__(self, attr):
        fcn = getattr(logger.getLogger(''), attr)
        def f2(msg, *args, **kwargs):
            return fcn("%s %s"%(self.socketinfo, str(msg)), *args, **kwargs)
        return f2