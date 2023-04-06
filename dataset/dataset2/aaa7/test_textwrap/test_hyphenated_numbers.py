import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_hyphenated_numbers():
    text = 'Python 1.0.0 was released on 1994-01-26.  Python 1.0.1 was\nreleased on 1994-02-15.'
    WrapTestCase.check_wrap(text, 30, ['Python 1.0.0 was released on', '1994-01-26.  Python 1.0.1 was', 'released on 1994-02-15.'])
    WrapTestCase.check_wrap(text, 40, ['Python 1.0.0 was released on 1994-01-26.', 'Python 1.0.1 was released on 1994-02-15.'])
    WrapTestCase.check_wrap(text, 1, text.split(), break_long_words=False)
    text = 'I do all my shopping at 7-11.'
    WrapTestCase.check_wrap(text, 25, ['I do all my shopping at', '7-11.'])
    WrapTestCase.check_wrap(text, 27, ['I do all my shopping at', '7-11.'])
    WrapTestCase.check_wrap(text, 29, ['I do all my shopping at 7-11.'])
    WrapTestCase.check_wrap(text, 1, text.split(), break_long_words=False)

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_hyphenated_numbers()
