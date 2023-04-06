import _elementtree as et

b = et.TreeBuilder(element_factory=lambda x, y: 123)

b.start("tag", {})
b.data("ABCD")
b.start("tag2", {})