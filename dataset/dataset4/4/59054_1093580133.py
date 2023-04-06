from xml.etree import ElementTree as etree
class xetree:
	cElement = etree.Element
	class Element(etree.Element):
		def __init__(self, tag, attrib=None):
			xetree.cElement.__init__(self, tag, attrib)

etree.Element = xetree.Element

e = etree.Element("test", {'foobar':'bar'})
e.text = "failure"
print(etree.tostring(e))
# will lack "failure"