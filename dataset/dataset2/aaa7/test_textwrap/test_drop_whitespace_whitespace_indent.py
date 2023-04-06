import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_drop_whitespace_whitespace_indent():
    WrapTestCase.check_wrap('abcd efgh', 6, ['  abcd', '  efgh'], initial_indent='  ', subsequent_indent='  ')

WrapTestCase = test_textwrap.WrapTestCase()
test_drop_whitespace_whitespace_indent()
