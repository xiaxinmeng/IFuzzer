
class ChainMap(collections.ChainMap):
    def get_where(self, key):
        for i, mapping in enumerate(self.maps):
            try:
                return i, mapping[key]             # can't use 'key in mapping' with defaultdict
            except KeyError:
                pass
        return self.__missing__(key)            # support subclasses that define __missing__
