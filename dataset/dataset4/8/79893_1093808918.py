def _le_from_lt(self, other, NotImplemented=NotImplemented):
     'Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).'
     op_result = self.__lt__(other)
     return op_result or self == other