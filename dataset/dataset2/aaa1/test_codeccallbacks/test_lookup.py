import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_lookup():
    CodecCallbackTest.assertEqual(codecs.strict_errors, codecs.lookup_error('strict'))
    CodecCallbackTest.assertEqual(codecs.ignore_errors, codecs.lookup_error('ignore'))
    CodecCallbackTest.assertEqual(codecs.strict_errors, codecs.lookup_error('strict'))
    CodecCallbackTest.assertEqual(codecs.xmlcharrefreplace_errors, codecs.lookup_error('xmlcharrefreplace'))
    CodecCallbackTest.assertEqual(codecs.backslashreplace_errors, codecs.lookup_error('backslashreplace'))
    CodecCallbackTest.assertEqual(codecs.namereplace_errors, codecs.lookup_error('namereplace'))

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_lookup()
