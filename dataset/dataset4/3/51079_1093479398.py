import collections
class __Helper(object):
  def __getitem__(self, ctor):
    return lambda: collections.defaultdict(lambda: ctor())
genericdefaultdict = __Helper()