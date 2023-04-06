class LibInfo( object ):
  """Library info taken from xml"""
  def __init__(self, libName=None, xmlName=None, packName=None):
    self.libName = libName
    self.xmlName = xmlName
    self.packName = packName

  def __repr__(self):
    return "L=%s X=%s P=%s" % (self.libName,self.xmlName,self.packName)

myObj = LibInfo("1", "2", "3")
logging.info("Simple data: %s", myObj)