import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_external_ges_default():
    parser = pulldom.parseString(test_pulldom.SMALL_SAMPLE)
    saxparser = parser.parser
    ges = saxparser.getFeature(feature_external_ges)
    PullDOMTestCase.assertEqual(ges, False)

PullDOMTestCase = test_pulldom.PullDOMTestCase()
test_external_ges_default()
