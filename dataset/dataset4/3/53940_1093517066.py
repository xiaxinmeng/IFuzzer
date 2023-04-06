# in Lib/abc.py
class ABCMeta(type):
    # ...

    def has_methods(cls, subclass):
        "Returns True iff subclass implements the appropriate methods"
        # ...