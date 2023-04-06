from collections import OrderedDict
od = OrderedDict()
class K(str):
    def __hash__(self):
        return 1