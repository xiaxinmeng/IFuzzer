import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_break_on_hyphens():
    text = 'yaba daba-doo'
    WrapTestCase.check_wrap(text, 10, ['yaba daba-', 'doo'], break_on_hyphens=True)
    WrapTestCase.check_wrap(text, 10, ['yaba', 'daba-doo'], break_on_hyphens=False)

WrapTestCase = test_textwrap.WrapTestCase()
test_break_on_hyphens()
