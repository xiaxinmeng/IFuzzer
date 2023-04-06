import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_placeholder_backtrack():
    text = 'Good grief Python features are advancing quickly!'
    MaxLinesTestCase.check_wrap(text, 12, ['Good grief', 'Python*****'], max_lines=3, placeholder='*****')

MaxLinesTestCase = test_textwrap.MaxLinesTestCase()
test_placeholder_backtrack()
