import _elementtree as et

state = {
    "tag": "tag",
    "_children": [],
    "attrib": "attr",
    "tail": "tail",
    "text": "text",
}

class X:
    def __hash__(self):
        e.__setstate__(state) # this frees e->extra->attrib
        return 13

e = et.Element("elem", {1: 2})
e.get(X())