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

def test_xmlgen_encoding():
    encodings = ('iso-8859-15', 'utf-8', 'utf-8-sig', 'utf-16', 'utf-16be', 'utf-16le', 'utf-32', 'utf-32be', 'utf-32le')
    for encoding in encodings:
        result = XmlgenTest.ioclass()
        gen = XMLGenerator(result, encoding=encoding)
        gen.startDocument()
        gen.startElement('doc', {'a': '€'})
        gen.characters('€')
        gen.endElement('doc')
        gen.endDocument()
        XmlgenTest.assertEqual(result.getvalue(), XmlgenTest.xml('<doc a="€">€</doc>', encoding=encoding))

XmlgenTest = test_sax.XmlgenTest()
test_xmlgen_encoding()
