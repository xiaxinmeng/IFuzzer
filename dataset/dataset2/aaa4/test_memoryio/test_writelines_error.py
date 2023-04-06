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

def test_writelines_error():
    memio = MemoryTestMixin.ioclass()

    def error_gen():
        yield MemoryTestMixin.buftype('spam')
        raise KeyboardInterrupt
    MemoryTestMixin.assertRaises(KeyboardInterrupt, memio.writelines, error_gen())

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_writelines_error()
