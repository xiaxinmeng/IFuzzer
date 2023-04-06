def __init__(self, a, b=_HAS_DEFAULT_FACTORY):
   self.a = a
   self.b = dict() if b is _HAS_DEFAULT_FACTORY else b