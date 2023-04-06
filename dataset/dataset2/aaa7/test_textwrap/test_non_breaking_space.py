import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_non_breaking_space():
    text = 'This is a sentence with non-breaking\xa0space.'
    WrapTestCase.check_wrap(text, 20, ['This is a sentence', 'with non-', 'breaking\xa0space.'], break_on_hyphens=True)
    WrapTestCase.check_wrap(text, 20, ['This is a sentence', 'with', 'non-breaking\xa0space.'], break_on_hyphens=False)

WrapTestCase = test_textwrap.WrapTestCase()
test_non_breaking_space()
