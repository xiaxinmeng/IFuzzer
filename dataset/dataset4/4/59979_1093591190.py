import xml.parsers.expat

class StopParsing(Exception):
    pass

def findFirstElementByName(data, what):
  def end_element(name):
      if name == what:
          raise StopParsing(name)

  p = xml.parsers.expat.ParserCreate()
  p.EndElementHandler = end_element