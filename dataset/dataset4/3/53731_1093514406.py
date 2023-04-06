import xml.etree.ElementTree as etree
xml_tree = etree.ElementTree(in_filehandle)
# process the tree
xml_tree.write(out_filehandle, encoding=xml_tree.encoding)