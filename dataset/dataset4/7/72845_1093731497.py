import xml.etree.cElementTree as ET

events = ET.Element('Events')
tree = ET.ElementTree(events)
tree.write('test.xml', xml_declaration=True, encoding='UTF-8')