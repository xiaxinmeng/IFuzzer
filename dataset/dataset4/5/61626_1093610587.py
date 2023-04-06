from inspect import Parameter, Signature

def make_signature(names):
   return Signature(
         Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class Structure:
   __signature__ = make_signature([])
   def __init__(self, *args, **kwargs):
      bound = self.__signature__.bind(*args, **kwargs)
      for name, val in bound.arguments.items():
         setattr(self, name, val)

class Stock(Structure):
   __signature__ = make_signature(['name', 'shares', 'price'])

pyth = Stock('PYTH', 100, 50)
help(pyth.__init__)