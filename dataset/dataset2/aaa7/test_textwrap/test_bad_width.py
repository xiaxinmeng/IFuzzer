import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_bad_width():
    text = "Whatever, it doesn't matter."
    WrapTestCase.assertRaises(ValueError, wrap, text, 0)
    WrapTestCase.assertRaises(ValueError, wrap, text, -1)

WrapTestCase = test_textwrap.WrapTestCase()
test_bad_width()
