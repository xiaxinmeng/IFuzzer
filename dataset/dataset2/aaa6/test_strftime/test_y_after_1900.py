import calendar
import sys
import re
from test import support
import time
import unittest

from locale import setlocale, LC_TIME
import test_strftime

def test_y_after_1900():
    Y1900Tests.assertEqual(time.strftime('%y', (2013, 1, 1, 0, 0, 0, 0, 0, 0)), '13')

Y1900Tests = test_strftime.Y1900Tests()
test_y_after_1900()
