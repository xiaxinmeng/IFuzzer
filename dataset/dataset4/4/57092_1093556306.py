from xml.sax.xmlreader import AttributesImpl as Attrs
from xml.sax.saxutils import XMLGenerator as Gen

g = Gen()
a = Attrs(dict([('k1','v1'),('','v_for_empty_name')]))
g.startDocument()
g.startElement('root',a)
g.endElement('root')
g.endDocument()
print