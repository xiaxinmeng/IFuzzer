import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_getitem_deprecation():
    parser = pulldom.parseString(test_pulldom.SMALL_SAMPLE)
    with PullDOMTestCase.assertWarnsRegex(DeprecationWarning, 'Use iterator protocol instead'):
        PullDOMTestCase.assertEqual(parser[-1][0], pulldom.START_DOCUMENT)

PullDOMTestCase = test_pulldom.PullDOMTestCase()
test_getitem_deprecation()
