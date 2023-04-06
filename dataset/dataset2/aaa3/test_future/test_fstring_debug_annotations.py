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

def test_fstring_debug_annotations():
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=:}'", expected="f'x={x:}'")
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=:.2f}'", expected="f'x={x:.2f}'")
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=!a}'", expected="f'x={x!a}'")
    AnnotationsFutureTestCase.assertAnnotationEqual("f'{x=!s:*^20}'", expected="f'x={x!s:*^20}'")

AnnotationsFutureTestCase = test_future.AnnotationsFutureTestCase()
test_fstring_debug_annotations()
