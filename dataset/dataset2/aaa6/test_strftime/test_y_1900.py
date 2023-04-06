import calendar
import sys
import re
from test import support
import time
import unittest

from locale import setlocale, LC_TIME
import test_strftime

def test_y_1900():
    Y1900Tests.assertEqual(time.strftime('%y', (1900, 1, 1, 0, 0, 0, 0, 0, 0)), '00')

Y1900Tests = test_strftime.Y1900Tests()
test_y_1900()
