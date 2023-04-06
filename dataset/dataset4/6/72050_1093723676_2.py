import _elementtree as et

state = {
    "tag": "tag",
    "_children": [1,2,3],
    "attrib": "attr",
    "tail": "tail",
    "text": "text",
}

e = et.Element("ttt")
e.__setstate__(state)

for x in e.iter():
    print(x)