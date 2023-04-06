
class Foo:
 def getx(self):
  return 5
 x = property(getx, doc='document the x property')
