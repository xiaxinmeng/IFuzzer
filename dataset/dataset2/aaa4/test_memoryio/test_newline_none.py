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

def test_newline_none():
    memio = TextIOTestMixin.ioclass('a\nb\r\nc\rd', newline=None)
    TextIOTestMixin.assertEqual(list(memio), ['a\n', 'b\n', 'c\n', 'd'])
    memio.seek(0)
    TextIOTestMixin.assertEqual(memio.read(1), 'a')
    TextIOTestMixin.assertEqual(memio.read(2), '\nb')
    TextIOTestMixin.assertEqual(memio.read(2), '\nc')
    TextIOTestMixin.assertEqual(memio.read(1), '\n')
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\nc\nd')
    memio = TextIOTestMixin.ioclass(newline=None)
    TextIOTestMixin.assertEqual(2, memio.write('a\n'))
    TextIOTestMixin.assertEqual(3, memio.write('b\r\n'))
    TextIOTestMixin.assertEqual(3, memio.write('c\rd'))
    memio.seek(0)
    TextIOTestMixin.assertEqual(memio.read(), 'a\nb\nc\nd')
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\nc\nd')
    memio = TextIOTestMixin.ioclass('a\r\nb', newline=None)
    TextIOTestMixin.assertEqual(memio.read(3), 'a\nb')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newline_none()
