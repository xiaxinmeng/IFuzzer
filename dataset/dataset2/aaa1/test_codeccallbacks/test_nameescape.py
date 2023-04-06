import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_nameescape():
    sin = 'a¬ሴ€耀\U0010ffff'
    sout = b'a\\N{NOT SIGN}\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('ascii', 'namereplace'), sout)
    sout = b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('latin-1', 'namereplace'), sout)
    sout = b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\xa4\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    CodecCallbackTest.assertEqual(sin.encode('iso-8859-15', 'namereplace'), sout)

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_nameescape()
