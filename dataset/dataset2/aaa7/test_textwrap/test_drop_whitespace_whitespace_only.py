import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_drop_whitespace_whitespace_only():
    WrapTestCase.check_wrap('  ', 6, [])

WrapTestCase = test_textwrap.WrapTestCase()
test_drop_whitespace_whitespace_only()
