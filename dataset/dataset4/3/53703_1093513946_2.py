element = ElementTree.fromstring("""<foo><bar>fööbar</bar></foo>""")
element_tree = ElementTree.ElementTree(element)

with open("bug2.xml", "w", encoding="US-ASCII") as f:
    element_tree.write(f)