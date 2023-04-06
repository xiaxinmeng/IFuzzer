import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_nobreak_long():
    LongWordTestCase.wrapper.break_long_words = 0
    LongWordTestCase.wrapper.width = 30
    expect = ['Did you say', '"supercalifragilisticexpialidocious?"', 'How *do* you spell that odd', 'word, anyways?']
    result = LongWordTestCase.wrapper.wrap(LongWordTestCase.text)
    LongWordTestCase.check(result, expect)
    result = wrap(LongWordTestCase.text, width=30, break_long_words=0)
    LongWordTestCase.check(result, expect)

LongWordTestCase = test_textwrap.LongWordTestCase()
LongWordTestCase.setUp()
test_nobreak_long()
