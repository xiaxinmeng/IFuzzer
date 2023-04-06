from xml.etree import ElementTree
text = ElementTree.Element('text')
text.text = 'f&oo"b<a>r'
xml_string = ElementTree.tostring(text)
import xml.dom.minidom as minidom
xml_tree = minidom.parseString(xml_string)
output = xml_tree.toprettyxml(indent='  ')
assert output.splitlines()[1] == xml_string.decode('utf8')
print(output)