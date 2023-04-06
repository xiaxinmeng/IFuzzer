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

def test_newlines_property():
    memio = TextIOTestMixin.ioclass(newline=None)

    def force_decode():
        memio.seek(0)
        memio.read()
    TextIOTestMixin.assertEqual(memio.newlines, None)
    memio.write('a\n')
    force_decode()
    TextIOTestMixin.assertEqual(memio.newlines, '\n')
    memio.write('b\r\n')
    force_decode()
    TextIOTestMixin.assertEqual(memio.newlines, ('\n', '\r\n'))
    memio.write('c\rd')
    force_decode()
    TextIOTestMixin.assertEqual(memio.newlines, ('\r', '\n', '\r\n'))

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_newlines_property()
