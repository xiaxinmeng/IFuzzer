import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_unicodedecodeerror():
    CodecCallbackTest.check_exceptionobjectargs(UnicodeDecodeError, ['ascii', bytearray(b'g\xfcrk'), 1, 2, 'ouch'], "'ascii' codec can't decode byte 0xfc in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeDecodeError, ['ascii', bytearray(b'g\xfcrk'), 1, 3, 'ouch'], "'ascii' codec can't decode bytes in position 1-2: ouch")

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_unicodedecodeerror()
