from test import support
from test.support import os_helper
import array
import io
import marshal
import sys
import unittest
import os
import types
import _testcapi
import test_marshal

def test_sets():
    for constructor in (set, frozenset):
        ContainerTestCase.helper(constructor(ContainerTestCase.d.keys()))

ContainerTestCase = test_marshal.ContainerTestCase()
test_sets()
