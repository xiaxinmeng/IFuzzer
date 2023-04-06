from xml.dom import minidom
node = minidom.parseString("<o><i/>t</o>").documentElement
node.childNodes[1].nodeValue = ""
node.normalize()
assert node.childNodes[-1].nextSibling == None