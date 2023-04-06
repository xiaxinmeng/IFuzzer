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

def test_xmlgen_ns_empty():
    result = XmlgenTest.ioclass()
    gen = XMLGenerator(result, short_empty_elements=True)
    gen.startDocument()
    gen.startPrefixMapping('ns1', ns_uri)
    gen.startElementNS((ns_uri, 'doc'), 'ns1:doc', {})
    gen.startElementNS((None, 'udoc'), None, {})
    gen.endElementNS((None, 'udoc'), None)
    gen.endElementNS((ns_uri, 'doc'), 'ns1:doc')
    gen.endPrefixMapping('ns1')
    gen.endDocument()
    XmlgenTest.assertEqual(result.getvalue(), XmlgenTest.xml('<ns1:doc xmlns:ns1="%s"><udoc/></ns1:doc>' % ns_uri))

XmlgenTest = test_sax.XmlgenTest()
test_xmlgen_ns_empty()
