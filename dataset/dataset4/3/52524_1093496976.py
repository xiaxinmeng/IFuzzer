from xml.etree import ElementTree
with open( 'test.xml', 'r' ) as f:
    xml = ElementTree.parse( f )
ElementTree.dump( xml )