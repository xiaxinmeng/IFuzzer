import __future__
import ast
import unittest
from test import support
from test.support import import_helper
from textwrap import dedent
import os
import re
import sys
from test import future_test1
from test import future_test2
from test import test_future3

from test import test_future5
import test_future

def test_future2():
    with import_helper.CleanImport('future_test2'):
        from test import future_test2
        FutureTest.assertEqual(future_test2.result, 6)

FutureTest = test_future.FutureTest()
test_future2()
