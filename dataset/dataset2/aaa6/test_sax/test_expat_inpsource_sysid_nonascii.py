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

@test_sax.requires_nonascii_filenames
def test_expat_inpsource_sysid_nonascii():
    fname = os_helper.TESTFN_UNICODE
    shutil.copyfile(test_sax.TEST_XMLFILE, fname)
    ExpatReaderTest.addCleanup(os_helper.unlink, fname)
    parser = create_parser()
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser.setContentHandler(xmlgen)
    parser.parse(InputSource(fname))
    ExpatReaderTest.assertEqual(result.getvalue(), test_sax.xml_test_out)

ExpatReaderTest = test_sax.ExpatReaderTest()
test_expat_inpsource_sysid_nonascii()
