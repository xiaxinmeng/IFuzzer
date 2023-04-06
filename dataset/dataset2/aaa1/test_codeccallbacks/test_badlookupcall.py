import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_badlookupcall():
    CodecCallbackTest.assertRaises(TypeError, codecs.lookup_error)

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_badlookupcall()
