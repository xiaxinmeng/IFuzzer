from pickle import _Pickler as Pickler
class ForkingPickler(Pickler):
    dispatch = Pickler.dispatch.copy()