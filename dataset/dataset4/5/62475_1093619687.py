class A: pass
class B(A): pass

sup = super(B, B())
isinstance(sup, A)  # returns False