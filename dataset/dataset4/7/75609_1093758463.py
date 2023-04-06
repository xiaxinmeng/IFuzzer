class BadMemo:
    def get(*args):
        return None

import xml.etree.ElementTree
xml.etree.ElementTree.Element('foo').__deepcopy__(BadMemo())