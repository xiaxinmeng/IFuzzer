from test.support import import_fresh_module
import pickle, sys

C = import_fresh_module('xml.etree.ElementTree', fresh=['_elementtree'])
P = import_fresh_module('xml.etree.ElementTree', blocked=['_elementtree'])
e = C.Element('foo', bar=42)
e.text = "text goes here"
e.tail = "opposite of head"
C.SubElement(e, 'child').append(C.Element('grandchild'))
e.append(C.Element('child'))
e.findall('.//grandchild')[0].set('attr', 'other value')
sys.modules['xml.etree.ElementTree'] = C 
s = pickle.dumps(e)
s