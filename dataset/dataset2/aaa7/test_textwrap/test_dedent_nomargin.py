import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_dedent_nomargin():
    text = "Hello there.\nHow are you?\nOh good, I'm glad."
    DedentTestCase.assertUnchanged(text)
    text = 'Hello there.\n\nBoo!'
    DedentTestCase.assertUnchanged(text)
    text = 'Hello there.\n  This is indented.'
    DedentTestCase.assertUnchanged(text)
    text = 'Hello there.\n\n  Boo!\n'
    DedentTestCase.assertUnchanged(text)

DedentTestCase = test_textwrap.DedentTestCase()
test_dedent_nomargin()
