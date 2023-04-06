import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_unicodetranslateerror():
    CodecCallbackTest.check_exceptionobjectargs(UnicodeTranslateError, ['gürk', 1, 2, 'ouch'], "can't translate character '\\xfc' in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeTranslateError, ['gĀrk', 1, 2, 'ouch'], "can't translate character '\\u0100' in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeTranslateError, ['g\uffffrk', 1, 2, 'ouch'], "can't translate character '\\uffff' in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeTranslateError, ['g𐀀rk', 1, 2, 'ouch'], "can't translate character '\\U00010000' in position 1: ouch")
    CodecCallbackTest.check_exceptionobjectargs(UnicodeTranslateError, ['gürk', 1, 3, 'ouch'], "can't translate characters in position 1-2: ouch")

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_unicodetranslateerror()
