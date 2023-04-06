import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_do_not_break_long_words_or_on_hyphens():
    expected = ['We used enyzme', '2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate', 'synthase.']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text1, 50, expected, break_long_words=False, break_on_hyphens=False)
    expected = ['We used', 'enyzme', '2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate', 'synthase.']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text1, 10, expected, break_long_words=False, break_on_hyphens=False)
    expected = ['1234567890', '-123456789', '0--this_is', '_a_very_lo', 'ng_option_', 'indeed-', 'good-bye"']
    LongWordWithHyphensTestCase.check_wrap(LongWordWithHyphensTestCase.text2, 10, expected)

LongWordWithHyphensTestCase = test_textwrap.LongWordWithHyphensTestCase()
LongWordWithHyphensTestCase.setUp()
test_do_not_break_long_words_or_on_hyphens()
