from xml.etree import ElementTree as etree

void_elements = [
    "area", "base","br", "col", "embed", "hr", "img", 
    "input", "link", "meta", "param", "source", "track", "wbr"
]
for el in void_elements:
    el = etree.Element(el)
    print(etree.tostring(el, method="html", encoding="unicode"))