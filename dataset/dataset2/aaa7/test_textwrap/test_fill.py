import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_fill():
    expect = 'This paragraph will be filled, first\nwithout any indentation, and then with\nsome (including a hanging indent).'
    result = fill(IndentTestCases.text, 40)
    IndentTestCases.check(result, expect)

IndentTestCases = test_textwrap.IndentTestCases()
IndentTestCases.setUp()
test_fill()
