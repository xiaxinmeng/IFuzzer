import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_punct_hyphens():
    WrapTestCase.check_split("the 'wibble-wobble' widget", ['the', ' ', "'wibble-", "wobble'", ' ', 'widget'])
    WrapTestCase.check_split('the "wibble-wobble" widget', ['the', ' ', '"wibble-', 'wobble"', ' ', 'widget'])
    WrapTestCase.check_split('the (wibble-wobble) widget', ['the', ' ', '(wibble-', 'wobble)', ' ', 'widget'])
    WrapTestCase.check_split("the ['wibble-wobble'] widget", ['the', ' ', "['wibble-", "wobble']", ' ', 'widget'])
    WrapTestCase.check_split("what-d'you-call-it.", "what-d'you-|call-|it.".split('|'))

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_punct_hyphens()
