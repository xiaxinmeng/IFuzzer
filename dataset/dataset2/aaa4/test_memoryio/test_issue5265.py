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

def test_issue5265():
    memio = TextIOTestMixin.ioclass('a\r\nb\r\n', newline=None)
    TextIOTestMixin.assertEqual(memio.read(5), 'a\nb\n')
    TextIOTestMixin.assertEqual(memio.getvalue(), 'a\nb\n')

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_issue5265()
