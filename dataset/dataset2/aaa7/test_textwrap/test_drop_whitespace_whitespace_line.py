import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_drop_whitespace_whitespace_line():
    text = 'abcd    efgh'
    WrapTestCase.check_wrap(text, 6, ['abcd', '    ', 'efgh'], drop_whitespace=False)
    WrapTestCase.check_wrap(text, 6, ['abcd', 'efgh'])

WrapTestCase = test_textwrap.WrapTestCase()
test_drop_whitespace_whitespace_line()
