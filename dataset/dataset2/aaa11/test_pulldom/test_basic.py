import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_basic():
    """Ensure SAX2DOM can parse from a stream."""
    with io.StringIO(test_pulldom.SMALL_SAMPLE) as fin:
        sd = test_pulldom.SAX2DOMTestHelper(fin, xml.sax.make_parser(), len(test_pulldom.SMALL_SAMPLE))
        for (evt, node) in sd:
            if evt == pulldom.START_ELEMENT and node.tagName == 'html':
                break
        SAX2DOMTestCase.assertGreater(len(node.childNodes), 0)

SAX2DOMTestCase = test_pulldom.SAX2DOMTestCase()
test_basic()
