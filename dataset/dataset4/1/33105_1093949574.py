s="""<?xml version='1.0'?><?pi-foobar?><test></test>"""
import xml.dom.minidom
p=xml.dom.minidom.parseString(s)

stack_trace="""
Traceback (most recent call last):
  File "test.py", line 6, in ?
    p=xml.dom.minidom.parseString(s)
  File "/hosts/multimedia/ins2/linux2/lib/python2.0/xml/dom/minidom.py", line 45
2, in parseString
    return _doparse( pulldom.parseString, args, kwargs )
  File "/hosts/multimedia/ins2/linux2/lib/python2.0/xml/dom/minidom.py", line 44
3, in _doparse
    events.expandNode( rootNode )
  File "/hosts/multimedia/ins2/linux2/lib/python2.0/xml/dom/pulldom.py", line 14
2, in expandNode
    cur_node.parentNode.appendChild( cur_node )
  File "/hosts/multimedia/ins2/linux2/lib/python2.0/xml/dom/minidom.py", line 40
0, in appendChild
    raise TypeError, "Two document elements disallowed"
TypeError: Two document elements disallowed
"""