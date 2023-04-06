import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_placeholder():
    text = "Hello there, how are you this fine day? I'm glad to hear it!"
    MaxLinesTestCase.check_shorten(text, 17, 'Hello there,$$', placeholder='$$')
    MaxLinesTestCase.check_shorten(text, 18, 'Hello there, how$$', placeholder='$$')
    MaxLinesTestCase.check_shorten(text, 18, 'Hello there, $$', placeholder=' $$')
    MaxLinesTestCase.check_shorten(text, len(text), text, placeholder='$$')
    MaxLinesTestCase.check_shorten(text, len(text) - 1, "Hello there, how are you this fine day? I'm glad to hear$$", placeholder='$$')

MaxLinesTestCase = test_textwrap.MaxLinesTestCase()
MaxLinesTestCase.setUp()
test_placeholder()
