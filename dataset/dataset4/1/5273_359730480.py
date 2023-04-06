def with_metaclass(meta, *bases):
    # ...
    class metaclass(type):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

        @classmethod
        def __prepare__(cls, name, this_bases):
            return meta.__prepare__(name, bases)
return type.__new__(metaclass, 'temporary_class', (), {})