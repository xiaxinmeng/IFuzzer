import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_backslashescape():
    sin = 'a¬ሴ€耀\U0010ffff'
    sout = b'a\\xac\\u1234\\u20ac\\u8000\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('ascii', 'backslashreplace'), sout)
    sout = b'a\xac\\u1234\\u20ac\\u8000\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('latin-1', 'backslashreplace'), sout)
    sout = b'a\xac\\u1234\xa4\\u8000\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('iso-8859-15', 'backslashreplace'), sout)

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_backslashescape()
