import xml.sax
from xml.sax.handler import ContentHandler
class C(ContentHandler):
	def startElement(self, name, attrs):
		assert False

xml.sax.parse(xml_path, C())