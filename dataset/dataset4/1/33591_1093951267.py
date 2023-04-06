import pprint, __builtin__
class Writer:
    def __init__(self):
        self.pp = pprint.PrettyPrinter()

    def str(self, obj):
        return self.pp.pformat(obj)
__builtin__.str = Writer().str