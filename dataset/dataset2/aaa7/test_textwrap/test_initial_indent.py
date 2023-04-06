import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_initial_indent():
    expect = ['     This paragraph will be filled,', 'first without any indentation, and then', 'with some (including a hanging indent).']
    result = wrap(IndentTestCases.text, 40, initial_indent='     ')
    IndentTestCases.check(result, expect)
    expect = '\n'.join(expect)
    result = fill(IndentTestCases.text, 40, initial_indent='     ')
    IndentTestCases.check(result, expect)

IndentTestCases = test_textwrap.IndentTestCases()
IndentTestCases.setUp()
test_initial_indent()
