class SubOSError(OSError):

    def __init__(self, foo, os_error, /):
        self.foo = foo
        self.os_error = os_error
        super().__init__(os_error.errno, os_error.strerror)

    def __reduce__(self): # Custom __reduce__
        return (self.__class__, (self.foo, self.os_error ))

    def __reduce__(self): # OSError __reduce__
        return (self.__class__, (self.os_error.errno, self.os_error.strerror ))