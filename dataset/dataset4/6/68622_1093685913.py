class ItemsView(MappingView, Set):
    ...
    def __contains__(self, item):
        key, value = item
        try:
            v = self._mapping[key]
        except KeyError:
            return False
        else:
            return v == value
    ...