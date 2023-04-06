
class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        self = type.__new__(...)  # this is PyType_FromSpec
        # more stuff
