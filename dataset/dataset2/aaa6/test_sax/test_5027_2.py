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

def test_5027_2():
    result = XmlgenTest.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startPrefixMapping('a', 'http://example.com/ns')
    gen.startElementNS(('http://example.com/ns', 'g1'), 'g1', {})
    lang_attr = {('http://www.w3.org/XML/1998/namespace', 'lang'): 'en'}
    gen.startElementNS(('http://example.com/ns', 'g2'), 'g2', lang_attr)
    gen.characters('Hello')
    gen.endElementNS(('http://example.com/ns', 'g2'), 'g2')
    gen.endElementNS(('http://example.com/ns', 'g1'), 'g1')
    gen.endPrefixMapping('a')
    gen.endDocument()
    XmlgenTest.assertEqual(result.getvalue(), XmlgenTest.xml('<a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>'))

XmlgenTest = test_sax.XmlgenTest()
test_5027_2()
