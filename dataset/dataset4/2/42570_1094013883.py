import pprint

class MyPrettyPrinter(pprint.PrettyPrinter):
  def format(self, object, context, maxlevels, level):
    if isinstance(object, int):
      return hex(object), True, False
    else:
      return pprint.PrettyPrinter.format(self, object,
context, maxlevels, level)

mpp = MyPrettyPrinter()
mpp.pprint(range(50))