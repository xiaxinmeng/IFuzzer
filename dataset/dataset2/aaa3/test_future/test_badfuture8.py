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

def test_badfuture8():
    with FutureTest.assertRaises(SyntaxError) as cm:
        from test import badsyntax_future8
    FutureTest.check_syntax_error(cm.exception, 'badsyntax_future8', 3)

FutureTest = test_future.FutureTest()
test_badfuture8()
