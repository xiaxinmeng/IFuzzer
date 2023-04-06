import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_funky_hyphens():
    WrapTestCase.check_split('what the--hey!', ['what', ' ', 'the', '--', 'hey!'])
    WrapTestCase.check_split('what the--', ['what', ' ', 'the--'])
    WrapTestCase.check_split('what the--.', ['what', ' ', 'the--.'])
    WrapTestCase.check_split('--text--.', ['--text--.'])
    WrapTestCase.check_split('--option', ['--option'])
    WrapTestCase.check_split('--option-opt', ['--option-', 'opt'])
    WrapTestCase.check_split('foo --option-opt bar', ['foo', ' ', '--option-', 'opt', ' ', 'bar'])

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_funky_hyphens()
