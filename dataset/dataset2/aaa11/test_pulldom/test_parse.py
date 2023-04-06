import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

def test_parse():
    """Minimal test of DOMEventStream.parse()"""
    handler = pulldom.parse(test_pulldom.tstfile)
    PullDOMTestCase.addCleanup(handler.stream.close)
    list(handler)
    with open(test_pulldom.tstfile, 'rb') as fin:
        list(pulldom.parse(fin))

PullDOMTestCase = test_pulldom.PullDOMTestCase()
test_parse()
