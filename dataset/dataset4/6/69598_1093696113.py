from fractions import Fraction
import operator

class Goo:
    __radd__, __rdivmod__, __rfloordiv__, __rmod__, __rmul__, __rpow__, __rsub__, __rtruediv__ = [lambda a, b: 'ok'] * 8