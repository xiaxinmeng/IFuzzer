class NDArrayOperatorsMixin:
    def __add__(self, other):
        return self._calculate(np.add, self, other)
    def __radd__(self, other):
        return self._calculate(np.add, other, self)
    ...  # repeat for all special methods

class A(NDArrayOperatorsMixin):
    def _calculate(self, op, *args):
        if not all(isinstance(arg, A) for arg in args):
            return NotImplemented
        ...  # implement calculation

class B(A):
    def _calculate(self, op, *args):
        ...  # something different