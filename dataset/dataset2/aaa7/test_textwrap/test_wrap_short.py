import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_wrap_short():
    text = 'This is a\nshort paragraph.'
    WrapTestCase.check_wrap(text, 20, ['This is a short', 'paragraph.'])
    WrapTestCase.check_wrap(text, 40, ['This is a short paragraph.'])

WrapTestCase = test_textwrap.WrapTestCase()
test_wrap_short()
