import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_translatehelper():

    class D(dict):

        def __getitem__(CodecCallbackTest, key):
            raise ValueError
    CodecCallbackTest.assertRaises(ValueError, 'ÿ'.translate, {255: sys.maxunicode + 1})
    CodecCallbackTest.assertRaises(TypeError, 'ÿ'.translate, {255: ()})

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_translatehelper()
