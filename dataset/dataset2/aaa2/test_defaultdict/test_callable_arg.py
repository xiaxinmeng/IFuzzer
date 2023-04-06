import os
import copy
import pickle
import tempfile
import unittest
from collections import defaultdict
import test_defaultdict

def test_callable_arg():
    TestDefaultDict.assertRaises(TypeError, defaultdict, {})

TestDefaultDict = test_defaultdict.TestDefaultDict()
test_callable_arg()
