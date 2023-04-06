class meta(type):
    def __len__(cls):
        return 12

class B:
    __metaclass__ = B