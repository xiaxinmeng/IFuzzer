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

def test_5027_1():
    test_xml = StringIO('<?xml version="1.0"?><a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>')
    parser = make_parser()
    parser.setFeature(feature_namespaces, True)
    result = XmlgenTest.ioclass()
    gen = XMLGenerator(result)
    parser.setContentHandler(gen)
    parser.parse(test_xml)
    XmlgenTest.assertEqual(result.getvalue(), XmlgenTest.xml('<a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>'))

XmlgenTest = test_sax.XmlgenTest()
test_5027_1()
