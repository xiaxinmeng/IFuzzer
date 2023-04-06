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

def test_expat_external_dtd_enabled():
    ExpatReaderTest.addCleanup(urllib.request.urlcleanup)
    parser = create_parser()
    parser.setFeature(feature_external_ges, True)
    resolver = ExpatReaderTest.TestEntityRecorder()
    parser.setEntityResolver(resolver)
    with ExpatReaderTest.assertRaises(URLError):
        parser.feed('<!DOCTYPE external SYSTEM "unsupported://non-existing">\n')
    ExpatReaderTest.assertEqual(resolver.entities, [(None, 'unsupported://non-existing')])

ExpatReaderTest = test_sax.ExpatReaderTest()
test_expat_external_dtd_enabled()
