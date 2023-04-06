import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_simple():
    text = "Hello there, how are you this fine day? I'm glad to hear it!"
    WrapTestCase.check_shorten(text, 18, 'Hello there, [...]')
    WrapTestCase.check_shorten(text, len(text), text)
    WrapTestCase.check_shorten(text, len(text) - 1, "Hello there, how are you this fine day? I'm glad to [...]")

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_simple()
