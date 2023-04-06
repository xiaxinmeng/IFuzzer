import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_unicodeencodeerror():
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'gürk', 1, 2, 'ouch'], "'ascii' codec can't encode character '\\xfc' in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'gürk', 1, 4, 'ouch'], "'ascii' codec can't encode characters in position 1-3: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'üx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\xfc' in position 0: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'Āx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\u0100' in position 0: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', '\uffffx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\uffff' in position 0: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', '𐀀x', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\U00010000' in position 0: ouch")

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_unicodeencodeerror()
