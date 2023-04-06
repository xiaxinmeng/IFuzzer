import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_hyphenated():
    text = "this-is-a-useful-feature-for-reformatting-posts-from-tim-peters'ly"
    WrapTestCase.check_wrap(text, 40, ['this-is-a-useful-feature-for-', "reformatting-posts-from-tim-peters'ly"])
    WrapTestCase.check_wrap(text, 41, ['this-is-a-useful-feature-for-', "reformatting-posts-from-tim-peters'ly"])
    WrapTestCase.check_wrap(text, 42, ['this-is-a-useful-feature-for-reformatting-', "posts-from-tim-peters'ly"])
    expect = "this-|is-|a-|useful-|feature-|for-|reformatting-|posts-|from-|tim-|peters'ly".split('|')
    WrapTestCase.check_wrap(text, 1, expect, break_long_words=False)
    WrapTestCase.check_split(text, expect)
    WrapTestCase.check_split('e-mail', ['e-mail'])
    WrapTestCase.check_split('Jelly-O', ['Jelly-O'])
    WrapTestCase.check_split('half-a-crown', 'half-|a-|crown'.split('|'))

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_hyphenated()
