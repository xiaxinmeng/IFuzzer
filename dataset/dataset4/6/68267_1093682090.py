import xml.etree.ElementTree as ET
root3 = ET.fromstring('<a><b/>TEXT</a>')
print(root3.text)