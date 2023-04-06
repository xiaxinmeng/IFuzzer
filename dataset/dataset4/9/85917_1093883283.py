

def _new_and_init(cls):
    inst = cls.__new__(cls)
    OrderedDict.__init__(inst)
    return inst


class A(OrderedDict):

    def __reduce__(self):
        # This fixes a bug in Python 3.6
        ret = list(super().__reduce__())

        ret[0] = _new_and_init
        ret[1] = (self.__class__, )

        return tuple(ret)

