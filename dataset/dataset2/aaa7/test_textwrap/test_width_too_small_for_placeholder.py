import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_width_too_small_for_placeholder():
    shorten('x' * 20, width=8, placeholder='(......)')
    with ShortenTestCase.assertRaises(ValueError):
        shorten('x' * 20, width=8, placeholder='(.......)')

ShortenTestCase = test_textwrap.ShortenTestCase()
test_width_too_small_for_placeholder()
