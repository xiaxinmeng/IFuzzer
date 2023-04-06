import sys
import os
import shutil
import importlib
import importlib.util
import unittest
from test.support import verbose
from test.support.os_helper import create_empty_file
from reprlib import repr as r
from reprlib import Repr
from reprlib import recursive_repr
from array import array
from collections import deque

from functools import WRAPPER_ASSIGNMENTS as assigned
import test_reprlib

def test_nesting():
    eq = ReprTests.assertEqual
    eq(r([[[[[[[]]]]]]]), '[[[[[[[]]]]]]]')
    eq(r([[[[[[[[]]]]]]]]), '[[[[[[[...]]]]]]]')
    eq(r(test_reprlib.nestedTuple(6)), '(((((((),),),),),),)')
    eq(r(test_reprlib.nestedTuple(7)), '(((((((...),),),),),),)')
    eq(r({test_reprlib.nestedTuple(5): test_reprlib.nestedTuple(5)}), '{((((((),),),),),): ((((((),),),),),)}')
    eq(r({test_reprlib.nestedTuple(6): test_reprlib.nestedTuple(6)}), '{((((((...),),),),),): ((((((...),),),),),)}')
    eq(r([[[[[[{}]]]]]]), '[[[[[[{}]]]]]]')
    eq(r([[[[[[[{}]]]]]]]), '[[[[[[[...]]]]]]]')

ReprTests = test_reprlib.ReprTests()
test_nesting()
