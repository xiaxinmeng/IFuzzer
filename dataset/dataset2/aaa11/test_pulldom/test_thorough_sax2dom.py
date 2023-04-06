import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_thorough_sax2dom():
    """Test some of the hard-to-reach parts of SAX2DOM."""
    pd = test_pulldom.SAX2DOMTestHelper(None, test_pulldom.SAX2DOMExerciser(), 12)
    ThoroughTestCase._test_thorough(pd, False)

ThoroughTestCase = test_pulldom.ThoroughTestCase()
test_thorough_sax2dom()
