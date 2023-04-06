import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_badandgoodstrictexceptions():
    CodecCallbackTest.assertRaises(TypeError, codecs.strict_errors, 42)
    CodecCallbackTest.assertRaises(Exception, codecs.strict_errors, Exception('ouch'))
    CodecCallbackTest.assertRaises(UnicodeEncodeError, codecs.strict_errors, UnicodeEncodeError('ascii', 'あ', 0, 1, 'ouch'))
    CodecCallbackTest.assertRaises(UnicodeDecodeError, codecs.strict_errors, UnicodeDecodeError('ascii', bytearray(b'\xff'), 0, 1, 'ouch'))
    CodecCallbackTest.assertRaises(UnicodeTranslateError, codecs.strict_errors, UnicodeTranslateError('あ', 0, 1, 'ouch'))

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_badandgoodstrictexceptions()
