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

def test_lone_surrogates():
    memio = PyStringIOTest.ioclass('\ud800')
    PyStringIOTest.assertEqual(memio.read(), '\ud800')
    memio = PyStringIOTest.ioclass()
    memio.write('\ud800')
    PyStringIOTest.assertEqual(memio.getvalue(), '\ud800')

PyStringIOTest = test_memoryio.PyStringIOTest()
test_lone_surrogates()
