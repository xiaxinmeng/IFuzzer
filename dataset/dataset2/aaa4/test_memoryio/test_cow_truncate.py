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

@support.cpython_only
def test_cow_truncate():

    def mutation(memio):
        memio.truncate(1)
    CBytesIOTest._test_cow_mutation(mutation)

CBytesIOTest = test_memoryio.CBytesIOTest()
test_cow_truncate()
