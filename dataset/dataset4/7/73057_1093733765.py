import xml.etree.cElementTree as ElementTree
y = x = ElementTree.Element('x')
for i in range(200000): y = ElementTree.SubElement(y, 'x')