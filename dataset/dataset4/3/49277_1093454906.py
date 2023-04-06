import xml.sax, xml.sax.saxutils
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 1)
c = xml.sax.saxutils.XMLGenerator()
parser.setContentHandler(c)
parser.parse('testfile.xml')