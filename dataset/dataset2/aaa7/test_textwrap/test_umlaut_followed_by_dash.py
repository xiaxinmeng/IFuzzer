import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_umlaut_followed_by_dash():
    text = 'aa ää-ää'
    WrapTestCase.check_wrap(text, 7, ['aa ää-', 'ää'])

WrapTestCase = test_textwrap.WrapTestCase()
test_umlaut_followed_by_dash()
