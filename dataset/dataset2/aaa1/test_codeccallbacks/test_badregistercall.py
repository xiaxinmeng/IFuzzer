import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_badregistercall():
    CodecCallbackTest.assertRaises(TypeError, codecs.register_error, 42)
    CodecCallbackTest.assertRaises(TypeError, codecs.register_error, 'test.dummy', 42)

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_badregistercall()
