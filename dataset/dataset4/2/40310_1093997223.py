class PyMeta(type):
    def __new__(meta, name, bases, attrs):
        return super(PyMeta, meta).__new__(meta,
                       name, bases, attrs)

class MetaTest(CMeta, PyMeta):
    pass

class Test:
    __metaclass__ = MetaTest