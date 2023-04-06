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

def test_1463026_3():
    result = XmlgenTest.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startPrefixMapping('my', 'qux')
    gen.startElementNS(('qux', 'a'), 'a', {(None, 'b'): 'c'})
    gen.endElementNS(('qux', 'a'), 'a')
    gen.endPrefixMapping('my')
    gen.endDocument()
    XmlgenTest.assertEqual(result.getvalue(), XmlgenTest.xml('<my:a xmlns:my="qux" b="c"></my:a>'))

XmlgenTest = test_sax.XmlgenTest()
test_1463026_3()
