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

def test_expat_dtdhandler():
    parser = create_parser()
    handler = ExpatReaderTest.TestDTDHandler()
    parser.setDTDHandler(handler)
    parser.feed('<!DOCTYPE doc [\n')
    parser.feed('  <!ENTITY img SYSTEM "expat.gif" NDATA GIF>\n')
    parser.feed('  <!NOTATION GIF PUBLIC "-//CompuServe//NOTATION Graphics Interchange Format 89a//EN">\n')
    parser.feed(']>\n')
    parser.feed('<doc></doc>')
    parser.close()
    ExpatReaderTest.assertEqual(handler._notations, [('GIF', '-//CompuServe//NOTATION Graphics Interchange Format 89a//EN', None)])
    ExpatReaderTest.assertEqual(handler._entities, [('img', None, 'expat.gif', 'GIF')])

ExpatReaderTest = test_sax.ExpatReaderTest()
test_expat_dtdhandler()
