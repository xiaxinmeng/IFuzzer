import errno
import os
import select
import subprocess
import sys
import textwrap
import unittest
from test import support
import test_select

def test_error_conditions():
    SelectTestCase.assertRaises(TypeError, select.select, 1, 2, 3)
    SelectTestCase.assertRaises(TypeError, select.select, [SelectTestCase.Nope()], [], [])
    SelectTestCase.assertRaises(TypeError, select.select, [SelectTestCase.Almost()], [], [])
    SelectTestCase.assertRaises(TypeError, select.select, [], [], [], 'not a number')
    SelectTestCase.assertRaises(ValueError, select.select, [], [], [], -1)

SelectTestCase = test_select.SelectTestCase()
test_error_conditions()
