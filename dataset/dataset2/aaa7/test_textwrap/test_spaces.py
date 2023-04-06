import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_spaces():
    MaxLinesTestCase.check_wrap(MaxLinesTestCase.text, 12, ['Hello there,', 'how are you', 'this fine', 'day? [...]'], max_lines=4)
    MaxLinesTestCase.check_wrap(MaxLinesTestCase.text, 6, ['Hello', '[...]'], max_lines=2)
    MaxLinesTestCase.check_wrap(MaxLinesTestCase.text + ' ' * 10, 12, ['Hello there,', 'how are you', 'this fine', "day?  I'm", 'glad to hear', 'it!'], max_lines=6)

MaxLinesTestCase = test_textwrap.MaxLinesTestCase()
test_spaces()
