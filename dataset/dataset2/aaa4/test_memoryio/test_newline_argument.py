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

def test_newline_argument():
    TextIOTestMixin.assertRaises(TypeError, TextIOTestMixin.ioclass, newline=b'\n')
    TextIOTestMixin.assertRaises(ValueError, TextIOTestMixin.ioclass, newline='error')
    for newline in (None, '', '\n', '\r', '\r\n'):
        TextIOTestMixin.ioclass(newline=newline)

TextIOTestMixin = test_memoryio.TextIOTestMixin()

test_newline_argument()
