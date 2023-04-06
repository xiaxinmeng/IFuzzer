
from xml.etree import ElementTree as et

XML_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE myelement>
"""

root = et.Element("myelement")
tree = et.ElementTree(root)

with open("myfile.xml", "w", encoding="iso-8859-1") as f:
    f.write(XML_HEADER)
    tree.write(f, encoding='unicode')
with open("myfile.xml", encoding="iso-8859-1") as f:
    print(f.read())
