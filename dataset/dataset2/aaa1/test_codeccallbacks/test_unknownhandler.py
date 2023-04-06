import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_unknownhandler():
    CodecCallbackTest.assertRaises(LookupError, codecs.lookup_error, 'test.unknown')

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_unknownhandler()
