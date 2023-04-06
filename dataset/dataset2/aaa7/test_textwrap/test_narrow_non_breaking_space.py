import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_narrow_non_breaking_space():
    text = 'This is a sentence with non-breaking\u202fspace.'
    WrapTestCase.check_wrap(text, 20, ['This is a sentence', 'with non-', 'breaking\u202fspace.'], break_on_hyphens=True)
    WrapTestCase.check_wrap(text, 20, ['This is a sentence', 'with', 'non-breaking\u202fspace.'], break_on_hyphens=False)

WrapTestCase = test_textwrap.WrapTestCase()
test_narrow_non_breaking_space()
