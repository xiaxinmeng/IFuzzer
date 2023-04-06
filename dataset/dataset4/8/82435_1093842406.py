import pickle

ose = OSError(1, 'unittest')

class SubOSError(OSError):

    def __init__(self, foo, os_error):
        super().__init__(os_error.errno, os_error.strerror)

cce = SubOSError(1, ose)
cce_pickled = pickle.dumps(cce)
pickle.loads(cce_pickled)