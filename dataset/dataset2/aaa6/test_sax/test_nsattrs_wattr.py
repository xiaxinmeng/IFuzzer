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

def test_nsattrs_wattr():
    attrs = AttributesNSImpl({(test_sax.ns_uri, 'attr'): 'val'}, {(test_sax.ns_uri, 'attr'): 'ns:attr'})
    XmlReaderTest.assertEqual(attrs.getLength(), 1)
    XmlReaderTest.assertEqual(attrs.getNames(), [(test_sax.ns_uri, 'attr')])
    XmlReaderTest.assertEqual(attrs.getQNames(), ['ns:attr'])
    XmlReaderTest.assertEqual(len(attrs), 1)
    XmlReaderTest.assertIn((test_sax.ns_uri, 'attr'), attrs)
    XmlReaderTest.assertEqual(list(attrs.keys()), [(test_sax.ns_uri, 'attr')])
    XmlReaderTest.assertEqual(attrs.get((test_sax.ns_uri, 'attr')), 'val')
    XmlReaderTest.assertEqual(attrs.get((test_sax.ns_uri, 'attr'), 25), 'val')
    XmlReaderTest.assertEqual(list(attrs.items()), [((test_sax.ns_uri, 'attr'), 'val')])
    XmlReaderTest.assertEqual(list(attrs.values()), ['val'])
    XmlReaderTest.assertEqual(attrs.getValue((test_sax.ns_uri, 'attr')), 'val')
    XmlReaderTest.assertEqual(attrs.getValueByQName('ns:attr'), 'val')
    XmlReaderTest.assertEqual(attrs.getNameByQName('ns:attr'), (test_sax.ns_uri, 'attr'))
    XmlReaderTest.assertEqual(attrs[test_sax.ns_uri, 'attr'], 'val')
    XmlReaderTest.assertEqual(attrs.getQNameByName((test_sax.ns_uri, 'attr')), 'ns:attr')

XmlReaderTest = test_sax.XmlReaderTest()
test_nsattrs_wattr()
