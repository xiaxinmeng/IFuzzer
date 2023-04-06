
class BidictKeysView(t.KeysView[KT], t.ValuesView[KT]):
    """Since the keys of a bidict are the values of its inverse (and vice versa),
    the ValuesView result of calling *bi.values()* is also a KeysView of *bi.inverse*.
    """


dict_keys: t.Type[t.KeysView[t.Any]] = type({}.keys())
BidictKeysView.register(dict_keys)
