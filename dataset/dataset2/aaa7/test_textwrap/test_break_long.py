import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_break_long():
    LongWordTestCase.check_wrap(LongWordTestCase.text, 30, ['Did you say "supercalifragilis', 'ticexpialidocious?" How *do*', 'you spell that odd word,', 'anyways?'])
    LongWordTestCase.check_wrap(LongWordTestCase.text, 50, ['Did you say "supercalifragilisticexpialidocious?"', 'How *do* you spell that odd word, anyways?'])
    LongWordTestCase.check_wrap('-' * 10 + 'hello', 10, ['----------', '               h', '               e', '               l', '               l', '               o'], subsequent_indent=' ' * 15)
    LongWordTestCase.check_wrap(LongWordTestCase.text, 12, ['Did you say ', '"supercalifr', 'agilisticexp', 'ialidocious?', '" How *do*', 'you spell', 'that odd', 'word,', 'anyways?'])

LongWordTestCase = test_textwrap.LongWordTestCase()
LongWordTestCase.setUp()
test_break_long()
