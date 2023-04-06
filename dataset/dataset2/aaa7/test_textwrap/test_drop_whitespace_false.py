import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_drop_whitespace_false():
    text = ' This is a    sentence with     much whitespace.'
    WrapTestCase.check_wrap(text, 10, [' This is a', '    ', 'sentence ', 'with     ', 'much white', 'space.'], drop_whitespace=False)

WrapTestCase = test_textwrap.WrapTestCase()
test_drop_whitespace_false()
