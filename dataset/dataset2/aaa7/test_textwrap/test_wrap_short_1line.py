import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_wrap_short_1line():
    text = 'This is a short line.'
    WrapTestCase.check_wrap(text, 30, ['This is a short line.'])
    WrapTestCase.check_wrap(text, 30, ['(1) This is a short line.'], initial_indent='(1) ')

WrapTestCase = test_textwrap.WrapTestCase()
test_wrap_short_1line()
