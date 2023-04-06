import io
import unittest
import xml.sax
from xml.sax.xmlreader import AttributesImpl
from xml.sax.handler import feature_external_ges
from xml.dom import pulldom
from test.support import findfile
import test_pulldom

@unittest.expectedFailure
def test_comment():
    """PullDOM does not receive "comment" events."""
    items = pulldom.parseString(test_pulldom.SMALL_SAMPLE)
    for (evt, _) in items:
        if evt == pulldom.COMMENT:
            break
    else:
        PullDOMTestCase.fail('No comment was encountered')

PullDOMTestCase = test_pulldom.PullDOMTestCase()
test_comment()
