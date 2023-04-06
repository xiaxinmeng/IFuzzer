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

def test_filter_basic():
    result = BytesIO()
    gen = XMLGenerator(result)
    filter = XMLFilterBase()
    filter.setContentHandler(gen)
    filter.startDocument()
    filter.startElement('doc', {})
    filter.characters('content')
    filter.ignorableWhitespace(' ')
    filter.endElement('doc')
    filter.endDocument()
    XMLFilterBaseTest.assertEqual(result.getvalue(), test_sax.start + b'<doc>content </doc>')

XMLFilterBaseTest = test_sax.XMLFilterBaseTest()
test_filter_basic()
