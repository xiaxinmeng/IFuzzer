import errno
import os
import select
import subprocess
import sys
import textwrap
import unittest
from test import support
import test_select

def test_select_mutated():
    a = []

    class F:

        def fileno(SelectTestCase):
            del a[-1]
            return sys.__stdout__.fileno()
    a[:] = [F()] * 10
    SelectTestCase.assertEqual(select.select([], a, []), ([], a[:5], []))

SelectTestCase = test_select.SelectTestCase()
test_select_mutated()
