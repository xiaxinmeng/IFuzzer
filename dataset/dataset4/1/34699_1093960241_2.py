def _getElementsByTagNameNSHelper(parent, nsURI,
localName, rc):
    for node in parent.childNodes:
        if node.nodeType == Node.ELEMENT_NODE:
            if ((localName == "*" or node.localName ==
localName) and
                (nsURI == "*" or node.namespaceURI ==
nsURI)):
                rc.append(node)
            _getElementsByTagNameNSHelper(node, name, rc)