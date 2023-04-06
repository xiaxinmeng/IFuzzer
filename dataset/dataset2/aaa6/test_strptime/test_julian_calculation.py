import unittest
import time
import locale
import re
import os
import sys
from test import support
from test.support import skip_if_buggy_ucrt_strfptime
from datetime import date as datetime_date
import _strptime
import datetime
import test_strptime

@skip_if_buggy_ucrt_strfptime
def test_julian_calculation():
    format_string = '%Y %m %d %H %M %S %w %Z'
    result = _strptime._strptime_time(time.strftime(format_string, CalculationTests.time_tuple), format_string)
    CalculationTests.assertTrue(result.tm_yday == CalculationTests.time_tuple.tm_yday, 'Calculation of tm_yday failed; %s != %s' % (result.tm_yday, CalculationTests.time_tuple.tm_yday))

CalculationTests = test_strptime.CalculationTests()
CalculationTests.setUp()
test_julian_calculation()
