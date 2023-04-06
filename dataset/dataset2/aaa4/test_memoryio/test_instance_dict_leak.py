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

def test_instance_dict_leak():
    for _ in range(100):
        memio = MemoryTestMixin.ioclass()
        memio.foo = 1

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_instance_dict_leak()
