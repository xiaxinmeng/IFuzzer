import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_whitespace():
    text = '\n            This is a  paragraph that  already has\n            line breaks and \t tabs too.'
    WrapTestCase.check_shorten(text, 62, 'This is a paragraph that already has line breaks and tabs too.')
    WrapTestCase.check_shorten(text, 61, 'This is a paragraph that already has line breaks and [...]')
    WrapTestCase.check_shorten('hello      world!  ', 12, 'hello world!')
    WrapTestCase.check_shorten('hello      world!  ', 11, 'hello [...]')
    WrapTestCase.check_shorten('hello      world!  ', 10, '[...]')

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_whitespace()
