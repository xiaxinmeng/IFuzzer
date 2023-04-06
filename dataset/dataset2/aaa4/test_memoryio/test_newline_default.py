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

def test_newline_default():
    memio = TextIOTestMixin.ioclass('a\nb\r\nc\rd')
    TextIOTestMixin.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\rd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
    memio = TextIOTestMixin.ioclass()
    TextIOTestMixin.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    TextIOTestMixin.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\rd'])
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newline_default()
