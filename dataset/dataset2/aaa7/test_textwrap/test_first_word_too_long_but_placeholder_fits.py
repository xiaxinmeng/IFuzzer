import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_first_word_too_long_but_placeholder_fits():
    ShortenTestCase.check_shorten('Helloo', 5, '[...]')

ShortenTestCase = test_textwrap.ShortenTestCase()
test_first_word_too_long_but_placeholder_fits()
