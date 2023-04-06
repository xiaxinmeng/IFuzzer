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

def test_newline_crlf():
    memio = TextIOTestMixin.ioclass('a\nb\r\nc\rd', newline='\r\n')
    TextIOTestMixin.assertEqual(memio.read(), 'a\r\nb\r\r\nc\rd')
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\r\n', 'b\r\r\n', 'c\rd'])
    memio.seek(0)
    TextIOTestMixin.assertEqual(memio.readlines(), ['a\r\n', 'b\r\r\n', 'c\rd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\r\nb\r\r\nc\rd')
    memio = TextIOTestMixin.ioclass(newline='\r\n')
    TextIOTestMixin.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\r\n', 'b\r\r\n', 'c\rd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\r\nb\r\r\nc\rd')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newline_crlf()
