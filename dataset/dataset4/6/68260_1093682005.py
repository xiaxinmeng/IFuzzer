import xml.etree.ElementTree as ET
root1 = ET.fromstring('<a>TEXT</a>')
print(root1.text)
root2 = ET.fromstring('<a>TEXT<b/></a>')
print(root2.text)
root3 = ET.fromstring('<a><b/>TEXT</a>')
print(root3.text)