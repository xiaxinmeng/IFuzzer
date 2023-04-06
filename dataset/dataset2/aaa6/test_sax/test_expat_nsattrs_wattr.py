from xml.sax import make_parser, ContentHandler, SAXException, SAXReaderNotAvailable, SAXParseException
import unittest
from unittest import mock
from xml.sax.saxutils import XMLGenerator, escape, unescape, quoteattr, XMLFilterBase, prepare_input_source
from xml.sax.expatreader import create_parser
from xml.sax.handler import feature_namespaces, feature_external_ges, LexicalHandler
from xml.sax.xmlreader import InputSource, AttributesImpl, AttributesNSImpl
from io import BytesIO, StringIO
import codecs
import os.path
import shutil
import sys
from urllib.error import URLError
import urllib.request
from test.support import os_helper
from test.support import findfile, run_unittest
from test.support.os_helper import FakePath, TESTFN
from xml.sax import parse
from xml.sax import parseString
from xml.sax import make_parser
from xml.sax import make_parser
from xml.sax import make_parser
from xml.sax import make_parser
from xml.sax import make_parser
from xml.sax import make_parser
import test_sax

def test_expat_nsattrs_wattr():
    parser = create_parser(1)
    gather = ExpatReaderTest.AttrGatherer()
    parser.setContentHandler(gather)
    parser.feed("<doc xmlns:ns='%s' ns:attr='val'/>" % test_sax.ns_uri)
    parser.close()
    attrs = gather._attrs
    ExpatReaderTest.assertEqual(attrs.getLength(), 1)
    ExpatReaderTest.assertEqual(attrs.getNames(), [(test_sax.ns_uri, 'attr')])
    ExpatReaderTest.assertTrue(attrs.getQNames() == [] or attrs.getQNames() == ['ns:attr'])
    ExpatReaderTest.assertEqual(len(attrs), 1)
    ExpatReaderTest.assertIn((test_sax.ns_uri, 'attr'), attrs)
    ExpatReaderTest.assertEqual(attrs.get((test_sax.ns_uri, 'attr')), 'val')
    ExpatReaderTest.assertEqual(attrs.get((test_sax.ns_uri, 'attr'), 25), 'val')
    ExpatReaderTest.assertEqual(list(attrs.items()), [((test_sax.ns_uri, 'attr'), 'val')])
    ExpatReaderTest.assertEqual(list(attrs.values()), ['val'])
    ExpatReaderTest.assertEqual(attrs.getValue((test_sax.ns_uri, 'attr')), 'val')
    ExpatReaderTest.assertEqual(attrs[test_sax.ns_uri, 'attr'], 'val')

ExpatReaderTest = test_sax.ExpatReaderTest()
test_expat_nsattrs_wattr()
