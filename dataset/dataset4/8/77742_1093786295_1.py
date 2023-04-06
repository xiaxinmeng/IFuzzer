
from xml.etree import ElementTree

xml = ElementTree.Element('Person', Name='John')
print(xml.tostring(encoding='unicode', method='xml'))
# Output: <Person Name="John" />
