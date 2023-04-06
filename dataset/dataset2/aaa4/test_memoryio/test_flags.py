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

def test_flags():
    memio = MemoryTestMixin.ioclass()
    MemoryTestMixin.assertEqual(memio.writable(), True)
    MemoryTestMixin.assertEqual(memio.readable(), True)
    MemoryTestMixin.assertEqual(memio.seekable(), True)
    MemoryTestMixin.assertEqual(memio.isatty(), False)
    MemoryTestMixin.assertEqual(memio.closed, False)
    memio.close()
    MemoryTestMixin.assertRaises(ValueError, memio.writable)
    MemoryTestMixin.assertRaises(ValueError, memio.readable)
    MemoryTestMixin.assertRaises(ValueError, memio.seekable)
    MemoryTestMixin.assertRaises(ValueError, memio.isatty)
    MemoryTestMixin.assertEqual(memio.closed, True)

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_flags()
