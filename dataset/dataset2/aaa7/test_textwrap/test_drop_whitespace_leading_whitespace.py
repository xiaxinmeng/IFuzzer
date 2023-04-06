import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_drop_whitespace_leading_whitespace():
    text = ' This is a sentence with leading whitespace.'
    WrapTestCase.check_wrap(text, 50, [' This is a sentence with leading whitespace.'])
    WrapTestCase.check_wrap(text, 30, [' This is a sentence with', 'leading whitespace.'])

WrapTestCase = test_textwrap.WrapTestCase()
test_drop_whitespace_leading_whitespace()
