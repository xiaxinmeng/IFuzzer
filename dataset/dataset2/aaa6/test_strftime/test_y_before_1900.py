import calendar
import sys
import re
from test import support
import time
import unittest

from locale import setlocale, LC_TIME
import test_strftime

def test_y_before_1900():
    t = (1899, 1, 1, 0, 0, 0, 0, 0, 0)
    if sys.platform == 'win32' or sys.platform.startswith(('aix', 'sunos', 'solaris')):
        with Y1900Tests.assertRaises(ValueError):
            time.strftime('%y', t)
    else:
        Y1900Tests.assertEqual(time.strftime('%y', t), '99')

Y1900Tests = test_strftime.Y1900Tests()
test_y_before_1900()
