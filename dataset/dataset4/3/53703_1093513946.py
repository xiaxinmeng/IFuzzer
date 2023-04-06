import sys
from xml.etree import ElementTree

element = ElementTree.fromstring("""<foo><bar>foobar</bar></foo>""")
element_tree = ElementTree.ElementTree(element)