import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_subsequent_indent():
    expect = '  * This paragraph will be filled, first\n    without any indentation, and then\n    with some (including a hanging\n    indent).'
    result = fill(IndentTestCases.text, 40, initial_indent='  * ', subsequent_indent='    ')
    IndentTestCases.check(result, expect)

IndentTestCases = test_textwrap.IndentTestCases()
IndentTestCases.setUp()
test_subsequent_indent()
