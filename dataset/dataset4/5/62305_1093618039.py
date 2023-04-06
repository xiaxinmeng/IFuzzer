import xml.etree.ElementTree as ET
tree = ET.parse("myinput.xml")
tree.write("myoutput.xml", encoding="utf-16")