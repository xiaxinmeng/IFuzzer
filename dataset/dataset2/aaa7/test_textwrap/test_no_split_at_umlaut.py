import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_no_split_at_umlaut():
    text = 'Die Empfänger-Auswahl'
    WrapTestCase.check_wrap(text, 13, ['Die', 'Empfänger-', 'Auswahl'])

WrapTestCase = test_textwrap.WrapTestCase()
test_no_split_at_umlaut()
