from pickle import Pickler
class ForkingPickler(Pickler):
    dispatch = Pickler.dispatch.copy()