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

def test_textio_properties():
    memio = TextIOTestMixin.ioclass()
    TextIOTestMixin.assertIsNone(memio.encoding)
    TextIOTestMixin.assertIsNone(memio.errors)
    TextIOTestMixin.assertFalse(memio.line_buffering)

TextIOTestMixin = test_memoryio.TextIOTestMixin()
test_textio_properties()
