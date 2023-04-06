import xml.etree.ElementTree as ET

class XElement(ET.Element):
    def __init__(self, tag, attrib={}):
        ET.Element.__init__(self, tag, attrib)

e = XElement('test')
e.text = 'failure'

print(ET.tostring(e))