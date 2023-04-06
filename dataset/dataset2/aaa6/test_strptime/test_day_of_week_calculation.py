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
def test_day_of_week_calculation():
    format_string = '%Y %m %d %H %S %j %Z'
    result = _strptime._strptime_time(time.strftime(format_string, CalculationTests.time_tuple), format_string)
    CalculationTests.assertTrue(result.tm_wday == CalculationTests.time_tuple.tm_wday, 'Calculation of day of the week failed; %s != %s' % (result.tm_wday, CalculationTests.time_tuple.tm_wday))

CalculationTests = test_strptime.CalculationTests()
CalculationTests.setUp()
test_day_of_week_calculation()
