import codecs
import html.entities
import sys
import unicodedata
import unittest
import test_codeccallbacks

def test_bug828737():
    charmap = {ord('&'): '&amp;', ord('<'): '&lt;', ord('>'): '&gt;', ord('"'): '&quot;'}
    for n in (1, 10, 100, 1000):
        text = 'abc<def>ghi' * n
        text.translate(charmap)

CodecCallbackTest = test_codeccallbacks.CodecCallbackTest()
test_bug828737()
