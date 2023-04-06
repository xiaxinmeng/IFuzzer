import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_funky_parens():
    WrapTestCase.check_split('foo (--option) bar', ['foo', ' ', '(--option)', ' ', 'bar'])
    WrapTestCase.check_split('foo (bar) baz', ['foo', ' ', '(bar)', ' ', 'baz'])
    WrapTestCase.check_split('blah (ding dong), wubba', ['blah', ' ', '(ding', ' ', 'dong),', ' ', 'wubba'])

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_funky_parens()
