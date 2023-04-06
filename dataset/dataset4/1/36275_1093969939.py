class Complex(complex):
    def __mul__(self,other):
       other=Complex(other)
       t = complex.__mul__(self,other)
       return Complex(t.real,t.imag)
    __rmul__ = __mul__

    def __add__(self,other):
       other=Complex(other)
       return Complex(self.real.__add__
(other.real),self.imag.__add__(other.imag))
    __radd__ = __add__