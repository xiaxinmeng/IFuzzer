import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

@unittest.expectedFailure
def test_sax2dom_fail():
    """SAX2DOM can"t handle a PI before the root element."""
    pd = test_pulldom.SAX2DOMTestHelper(None, test_pulldom.SAXExerciser(), 12)
    ThoroughTestCase._test_thorough(pd)

ThoroughTestCase = test_pulldom.ThoroughTestCase()
test_sax2dom_fail()
