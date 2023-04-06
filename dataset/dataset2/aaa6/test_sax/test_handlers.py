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

def test_handlers():

    class TestLexicalHandler(LexicalHandler):

        def __init__(LexicalHandlerTest, test_harness, *args, **kwargs):
            super().__init__(*args, **kwargs)
            LexicalHandlerTest.test_harness = test_harness

        def startCDATA(LexicalHandlerTest):
            LexicalHandlerTest.test_harness.in_cdata = True

        def endCDATA(LexicalHandlerTest):
            LexicalHandlerTest.test_harness.in_cdata = False

    class TestCharHandler(ContentHandler):

        def __init__(LexicalHandlerTest, test_harness, *args, **kwargs):
            super().__init__(*args, **kwargs)
            LexicalHandlerTest.test_harness = test_harness

        def characters(LexicalHandlerTest, content):
            if content != '\n':
                h = LexicalHandlerTest.test_harness
                t = h.specified_chars[h.char_index]
                h.assertEqual(t[0], content)
                h.assertEqual(t[1], h.in_cdata)
                h.char_index += 1
    LexicalHandlerTest.parser = create_parser()
    LexicalHandlerTest.parser.setContentHandler(TestCharHandler(LexicalHandlerTest))
    LexicalHandlerTest.parser.setProperty('http://xml.org/sax/properties/lexical-handler', TestLexicalHandler(LexicalHandlerTest))
    source = InputSource()
    source.setCharacterStream(LexicalHandlerTest.test_data)
    LexicalHandlerTest.parser.parse(source)
    LexicalHandlerTest.assertFalse(LexicalHandlerTest.in_cdata)
    LexicalHandlerTest.assertEqual(LexicalHandlerTest.char_index, 2)

LexicalHandlerTest = test_sax.LexicalHandlerTest()
LexicalHandlerTest.setUp()
test_handlers()
