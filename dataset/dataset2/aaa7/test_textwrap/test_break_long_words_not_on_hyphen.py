import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_break_long_words_not_on_hyphen():
    expected = ['We used enyzme 2-succinyl-6-hydroxy-2,4-cyclohexad', 'iene-1-carboxylate synthase.']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text1, 50, expected, break_on_hyphens=False)
    expected = ['We used', 'enyzme 2-s', 'uccinyl-6-', 'hydroxy-2,', '4-cyclohex', 'adiene-1-c', 'arboxylate', 'synthase.']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text1, 10, expected, break_on_hyphens=False)
    expected = ['1234567890', '-123456789', '0--this_is', '_a_very_lo', 'ng_option_', 'indeed-', 'good-bye"']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text2, 10, expected)

LongWordWithHyphensTestCase = test_textwrap.LongWordWithHyphensTestCase()
LongWordWithHyphensTestCase.setUp()
test_break_long_words_not_on_hyphen()
