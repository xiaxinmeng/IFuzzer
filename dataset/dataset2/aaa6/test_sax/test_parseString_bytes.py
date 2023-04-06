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

def test_parseString_bytes():
    encodings = ('us-ascii', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be')
    for encoding in encodings:
        ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, encoding))
        ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, encoding, None))
    ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, 'utf-8-sig', 'utf-8'))
    ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, 'utf-8-sig', None))
    ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, 'iso-8859-1'))
    with ParseTest.assertRaises(SAXException):
        ParseTest.check_parseString(test_sax.xml_bytes(ParseTest.data, 'iso-8859-1', None))

ParseTest = test_sax.ParseTest()
test_parseString_bytes()
