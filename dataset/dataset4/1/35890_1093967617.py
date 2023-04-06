class Meta(type):
   def getname(self):
      return self._name + "!"

   def setname(self, name):
      self._name = name

   name = property(getname, setname)

class Element(object):
   __metaclass__ = Meta

   name = "test"