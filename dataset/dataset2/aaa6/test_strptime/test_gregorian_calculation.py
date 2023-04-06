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
def test_gregorian_calculation():
    format_string = '%Y %H %M %S %w %j %Z'
    result = _strptime._strptime_time(time.strftime(format_string, CalculationTests.time_tuple), format_string)
    CalculationTests.assertTrue(result.tm_year == CalculationTests.time_tuple.tm_year and result.tm_mon == CalculationTests.time_tuple.tm_mon and (result.tm_mday == CalculationTests.time_tuple.tm_mday), 'Calculation of Gregorian date failed; %s-%s-%s != %s-%s-%s' % (result.tm_year, result.tm_mon, result.tm_mday, CalculationTests.time_tuple.tm_year, CalculationTests.time_tuple.tm_mon, CalculationTests.time_tuple.tm_mday))

CalculationTests = test_strptime.CalculationTests()
CalculationTests.setUp()
test_gregorian_calculation()
