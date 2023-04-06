import os
import copy
import pickle
import tempfile
import unittest
from collections import defaultdict
import test_defaultdict

def test_recursive_repr():

    class sub(defaultdict):

        def __init__(TestDefaultDict):
            TestDefaultDict.default_factory = TestDefaultDict._factory

        def _factory(TestDefaultDict):
            return []
    d = sub()
    TestDefaultDict.assertRegex(repr(d), 'sub\\(<bound method .*sub\\._factory of sub\\(\\.\\.\\., \\{\\}\\)>, \\{\\}\\)')

TestDefaultDict = test_defaultdict.TestDefaultDict()
test_recursive_repr()
