import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_thorough_parse():
    """Test some of the hard-to-reach parts of PullDOM."""
    ThoroughTestCase._test_thorough(pulldom.parse(None, parser=test_pulldom.SAXExerciser()))

ThoroughTestCase = test_pulldom.ThoroughTestCase()
test_thorough_parse()
