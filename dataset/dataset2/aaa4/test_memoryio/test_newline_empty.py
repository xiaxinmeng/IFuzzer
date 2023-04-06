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

def test_newline_empty():
    memio = TextIOTestMixin.ioclass('a\nb\r\nc\rd', newline='')
    TextIOTestMixin.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\r', 'd'])
    memio.seek(0)
    TextIOTestMixin.assertEqual(memio.read(4), 'a\nb\r')
    TextIOTestMixin.assertEqual(memio.read(2), '\nc')
    TextIOTestMixin.assertEqual(memio.read(1), '\r')
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
    memio = TextIOTestMixin.ioclass(newline='')
    TextIOTestMixin.assertEqual(2, memio.write('a\n'))
    TextIOTestMixin.assertEqual(2, memio.write('b\r'))
    TextIOTestMixin.assertEqual(2, memio.write('\nc'))
    TextIOTestMixin.assertEqual(2, memio.write('\rd'))
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\r', 'd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newline_empty()
