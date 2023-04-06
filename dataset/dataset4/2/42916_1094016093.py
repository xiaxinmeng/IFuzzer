from xml.dom import minidom

def testme(xmltext):
    node = minidom.parseString(xmltext).documentElement
    for child in node.childNodes:
        if child.nodeValue == "t":
            child.nodeValue = ""
    node.normalize()

    child = node.firstChild
    while child:
        next = child.nextSibling
        if child.nodeType == child.TEXT_NODE and child.nodeValue == "":
            node.removeChild(child)
        child = next
    return node