import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_badandgoodignoreexceptions():
    CodecCallbackTest.assertRaises(TypeError, codecs.ignore_errors, 42)
    CodecCallbackTest.assertRaises(TypeError, codecs.ignore_errors, UnicodeError('ouch'))
    CodecCallbackTest.assertEqual(codecs.ignore_errors(UnicodeEncodeError('ascii', 'aあb', 1, 2, 'ouch')), ('', 2))
    CodecCallbackTest.assertEqual(codecs.ignore_errors(UnicodeDecodeError('ascii', bytearray(b'a\xffb'), 1, 2, 'ouch')), ('', 2))
    CodecCallbackTest.assertEqual(codecs.ignore_errors(UnicodeTranslateError('aあb', 1, 2, 'ouch')), ('', 2))

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_badandgoodignoreexceptions()
