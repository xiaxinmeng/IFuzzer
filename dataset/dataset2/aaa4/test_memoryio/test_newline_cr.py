import unittest
from test import support
import io
import _pyio as pyio
import pickle
import sys
import __main__
import array
import array
import test_memoryio

def test_newline_cr():
    memio = TextIOTestMixin.ioclass('a\nb\r\nc\rd', newline='\r')
    TextIOTestMixin.assertEqual(memio.read(), 'a\rb\r\rc\rd')
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\rb\r\rc\rd')
    memio = TextIOTestMixin.ioclass(newline='\r')
    TextIOTestMixin.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    memio.seek(0)
    TextIOTestMixin.assertEqual(memio.readlines(), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\rb\r\rc\rd')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newline_cr()
