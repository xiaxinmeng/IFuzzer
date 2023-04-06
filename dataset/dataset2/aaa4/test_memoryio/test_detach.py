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

def test_detach():
    buf = MemoryTestMixin.ioclass()
    MemoryTestMixin.assertRaises(MemoryTestMixin.UnsupportedOperation, buf.detach)

MemoryTestMixin = test_memoryio.MemoryTestMixin()

test_detach()
