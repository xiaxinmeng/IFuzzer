import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_split():
    text = 'Hello there -- you goof-ball, use the -b option!'
    result = WrapTestCase.wrapper._split(text)
    WrapTestCase.check(result, ['Hello', ' ', 'there', ' ', '--', ' ', 'you', ' ', 'goof-', 'ball,', ' ', 'use', ' ', 'the', ' ', '-b', ' ', 'option!'])

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_split()
