import xml.etree.ElementTree as ElementTree
with open('/srv/www/etc/signatures.xml','rt') as f:
    tree = ElementTree.parse(f)